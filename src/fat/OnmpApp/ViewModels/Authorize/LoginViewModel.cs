using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using OnmpApp.Models;
using OnmpApp.Helpers;
using OnmpApp.Services.Authorize;
using OnmpApp.Views.Authorize;

namespace OnmpApp.ViewModels.Authorize;

public partial class LoginViewModel : ObservableObject
{
    [ObservableProperty]
    string _email = new(Settings.Email);

    [ObservableProperty]
    string _password = Settings.Password;

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
        if (Settings.WasAuthorized)
            _ = Login();
    }

    [RelayCommand]
    async Task NavigateToInformationPage()
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

        // TODO: Убрать задержку
        await Task.Delay(1000);

        LoginService loginService = new();
        bool logined = await loginService.AuthenticateUser(Email, Password);
        if (!logined)
        {
            IsLoginingIn = false;
            InvalidUserDataOccured = true;
            return;
        }

        Settings.Email = Email;
        if (SavePassword)
            Settings.Password = Password;

        Settings.WasAuthorized = true;
        await Shell.Current.GoToAsync("//TabPage");
        IsLoginingIn = false;
    }
}
