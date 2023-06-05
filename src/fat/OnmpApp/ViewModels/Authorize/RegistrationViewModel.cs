using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using OnmpApp.Helpers;
using OnmpApp.Services;
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
        string _firstName;

        [ObservableProperty]
        string _lastName;

        [ObservableProperty]
        string _middleName;

        [ObservableProperty]
        [NotifyPropertyChangedFor(nameof(InvalidUserDataOccured))]
        bool _invalidEmailOccured = false;

        [ObservableProperty]
        [NotifyPropertyChangedFor(nameof(InvalidUserDataOccured))]
        bool _invalidPasswordOccured = false;

        [ObservableProperty]
        [NotifyPropertyChangedFor(nameof(InvalidUserDataOccured))]
        bool _invalidNameOccured = false;

        public bool InvalidUserDataOccured => InvalidEmailOccured || InvalidPasswordOccured || InvalidNameOccured;

        [ObservableProperty]
        string _errorText = Properties.Resources.InvalidUserData;

        public RegistrationViewModel() { }

        [ObservableProperty]
        bool _registering = false;
        [RelayCommand]
        async Task Register()
        {
            if(Registering) return;

            Registering = true;
            InvalidEmailOccured = false;
            InvalidPasswordOccured = false;

            // Проверка, что введен правильный Email
            if (!Email.IsEmail())
            {
                InvalidEmailOccured = true;
                ErrorText = Properties.Resources.InvalidEmailFormat;
                Registering = false;
                return;
            }

            // Проверка, что введен правильный пароль
            if (string.IsNullOrEmpty(FirstPassword) || FirstPassword != SecondPassword)
            {
                InvalidPasswordOccured = true;
                ErrorText = Properties.Resources.PasswordsDontMatch;
                Registering = false;
                return;
            }

            // Проверка, что введены имена
            if (string.IsNullOrEmpty(FirstName) || string.IsNullOrEmpty(LastName) || string.IsNullOrEmpty(MiddleName))
            {
                InvalidNameOccured = true;
                ErrorText = Properties.Resources.InvalidNames;
                Registering = false;
                return;
            }

            if (!await UserService.Register(Email, FirstPassword, FirstName, LastName, MiddleName))
            {
                InvalidEmailOccured = true;
                ErrorText = Properties.Resources.Error;
                Registering = false;
                return;
            }

            ToastHelper.Show(Properties.Resources.SuccessRegistration);
            await Shell.Current.GoToAsync("..");

            Registering = false;
        }

    }
}
