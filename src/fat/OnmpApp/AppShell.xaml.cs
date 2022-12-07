using OnmpApp.Views.Authorize;
using OnmpApp.Views.MainTabs;
using OnmpApp.Views.UserSettings;

namespace OnmpApp;

public partial class AppShell : Shell
{
	public AppShell()
	{
		InitializeComponent();

        Routing.RegisterRoute(nameof(LoginPage), typeof(LoginPage));
        Routing.RegisterRoute($"{nameof(LoginPage)}/{nameof(RegistrationPage)}", typeof(RegistrationPage));
        Routing.RegisterRoute($"{nameof(SearchTabPage)}/{nameof(SettingsPage)}", typeof(SettingsPage));
    }
}
