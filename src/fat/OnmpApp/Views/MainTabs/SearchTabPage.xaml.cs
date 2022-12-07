using OnmpApp.Controls;
using OnmpApp.ViewModels.MainTabs;

namespace OnmpApp.Views.MainTabs;

public partial class SearchTabPage : MasterContentPage
{
	public SearchTabPage(SearchTabViewModel vm)
	{
		InitializeComponent();
		BindingContext = vm;
	}
}