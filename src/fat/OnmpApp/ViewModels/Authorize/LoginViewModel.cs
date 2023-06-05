using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using OnmpApp.Database;
using OnmpApp.Models;
using OnmpApp.Helpers;
using OnmpApp.Services;
using OnmpApp.Views.Authorize;
using OnmpApp.Properties;


namespace OnmpApp.ViewModels.Authorize;

public partial class LoginViewModel : ObservableObject
{
    [ObservableProperty]
    string _email = new(Settings.Email);

    [ObservableProperty]
    string _password = new(Settings.Password);

    [ObservableProperty]
    bool _savePassword = true;

    [ObservableProperty] // Поле состояния запроса к серверу
    [NotifyPropertyChangedFor(nameof(IsNotLoginingIn))]
    bool _isLoginingIn = false;
    public bool IsNotLoginingIn { get => !IsLoginingIn;}

    [ObservableProperty] // Поле состояния ошибки при вводе данных пользователя
    bool _invalidUserDataOccured = false;

    [ObservableProperty]
    string _errorText = Properties.Resources.InvalidUserData;

    public LoginViewModel()
    {
        // Если ранее был успешный вход, попробовать войти со старыми данными
        if (!Settings.WasAuthorized) 
            return;

        if (Connectivity.NetworkAccess != NetworkAccess.Internet || (DateTime.Now - Settings.AuthorizedDate).TotalDays <= 1)
            _ = NavigateToMainPage();
        else
            _ = Login();
    }

    [RelayCommand]
    static void NavigateToInformationPage()
    {
        // TODO: Перейти на страницу информации приложения
    }

    /* Действие кнопки "восстановить"
    [RelayCommand]
    async Task NavigateToRestoringPasswordPage()
    {
        // Перейти на страницу восстановления пароля
    }*/

    [RelayCommand]
    async Task NavigateToRegistrationPage()
    {
        await Shell.Current.GoToAsync(nameof(RegistrationPage));
    }

    static async Task NavigateToMainPage()
    {
        await Shell.Current.GoToAsync("//TabPage");
    }

    [RelayCommand]
    async Task Login()
    {
        InvalidUserDataOccured = false;

        // Проверка, что введены правильные данные
        if (!Email.IsEmail() || string.IsNullOrWhiteSpace(Password))
        {
            InvalidUserDataOccured = true;
            return;
        }

        IsLoginingIn = true;

        if (!await UserService.Authenticate(Email, Password))
        {
            IsLoginingIn = false;
            InvalidUserDataOccured = true;
            return;
        }

        Settings.Email = Email;
        Settings.UserId = await UserService.GetId(Email);
        Settings.AuthorizedDate = DateTime.Now;

        if (SavePassword)
        {
            Settings.WasAuthorized = true;
            Settings.Password = Password;
        }

        _ = NavigateToMainPage();

        if ((DateTime.Now - Settings.CatalogSyncDate).TotalSeconds < 3 || (DateTime.Now - Settings.CatalogSyncDate).TotalDays >= 7)
        {
            await InitService.LoadCatalogNames();
            Settings.CatalogSyncDate = DateTime.Now;
        }
        IsLoginingIn = false;
    }
}
