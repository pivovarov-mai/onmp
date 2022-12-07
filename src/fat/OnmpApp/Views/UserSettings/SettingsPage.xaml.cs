using OnmpApp.Controls;
using OnmpApp.ViewModels.UserSettings;

namespace OnmpApp.Views.UserSettings;

public partial class SettingsPage : MasterContentPage
{
	public SettingsPage(SettingsViewModel vm)
	{
		InitializeComponent();
		this.BindingContext = vm;
	}
}