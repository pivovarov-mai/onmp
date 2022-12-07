using OnmpApp.Controls;
using OnmpApp.ViewModels.Authorize;

namespace OnmpApp.Views.Authorize;

public partial class RegistrationPage : MasterContentPage
{
	public RegistrationPage(RegistrationViewModel vm)
	{
		InitializeComponent();
		this.BindingContext = vm;
	}
}