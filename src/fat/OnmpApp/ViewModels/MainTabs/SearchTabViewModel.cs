using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using OnmpApp.Views.Authorize;
using OnmpApp.Views.UserSettings;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.ViewModels.MainTabs;

public partial class SearchTabViewModel : ObservableObject
{

    [RelayCommand]
    async Task NavigateToSettingsPage()
    {
        await Shell.Current.GoToAsync(nameof(SettingsPage));
    }
}
