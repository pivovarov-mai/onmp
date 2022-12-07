using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using OnmpApp.Views.Authorize;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.ViewModels.UserSettings;

public partial class SettingsViewModel : ObservableObject
{

    [RelayCommand]
    async Task LogOut()
    {
        OnmpApp.Settings.WasAuthorized = false;
        OnmpApp.Settings.Password = "";
        await Shell.Current.GoToAsync($"//{nameof(LoginPage)}");
    }
}
