using OnmpApp.Controls;
using OnmpApp.ViewModels.Authorize;

namespace OnmpApp.Views.Authorize;

public partial class LoginPage : MasterContentPage
{
    public LoginPage(LoginViewModel vm)
    {
        InitializeComponent();
        BindingContext = vm;
    }
}