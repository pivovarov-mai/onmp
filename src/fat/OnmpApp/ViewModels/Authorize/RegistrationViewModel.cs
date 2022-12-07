using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using OnmpApp.Helpers;
using OnmpApp.Services.Authorize;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.ViewModels.Authorize
{
    public partial class RegistrationViewModel : ObservableObject
    {
        [ObservableProperty]
        string _email;

        [ObservableProperty]
        string _firstPassword;

        [ObservableProperty]
        string _secondPassword;

        [ObservableProperty]
        [NotifyPropertyChangedFor(nameof(InvalidUserDataOccured))]
        bool _invalidEmailOccured = false;

        [ObservableProperty]
        [NotifyPropertyChangedFor(nameof(InvalidUserDataOccured))]
        bool _invalidPasswordOccured = false;
  
        public bool InvalidUserDataOccured => InvalidEmailOccured || InvalidPasswordOccured;

        [ObservableProperty]
        string _errorText = Properties.Resources.InvalidUserData;

        public RegistrationViewModel() { }

        [RelayCommand]
        async Task Register()
        {
            InvalidEmailOccured = false;
            InvalidPasswordOccured = false;

            // Проверка, что введен правильный Email
            if (!Email.IsEmail())
            {
                InvalidEmailOccured = true;
                ErrorText = Properties.Resources.InvalidEmailFormat;
                return;
            }

            // Проверка, что введен правильный пароль
            if (string.IsNullOrEmpty(FirstPassword) || FirstPassword != SecondPassword)
            {
                InvalidPasswordOccured = true;
                ErrorText = Properties.Resources.PasswordsDontMatch;
                return;
            }

            RegistrationService service = new();
            bool registered = await service.RegisterUser(Email, FirstPassword);
            if (!registered)
            {
                InvalidEmailOccured = true;
                ErrorText = Properties.Resources.EmailAlreadyExists;
                return;
            }

            ToastHelper.Show(Properties.Resources.SuccessRegistration);
            await Shell.Current.GoToAsync("..");
        }

    }
}
