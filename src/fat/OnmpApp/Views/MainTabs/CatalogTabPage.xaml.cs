using OnmpApp.Controls;
using OnmpApp.ViewModels.MainTabs;

namespace OnmpApp.Views.MainTabs;

public partial class CatalogTabPage : MasterContentPage
{

    public CatalogTabPage(CatalogTabViewModel vm)
	{
		InitializeComponent();
        BindingContext = vm;
    }

    bool searching = false;

    private async void SearchChanged(object sender, EventArgs e)
    {
        if ((BindingContext as CatalogTabViewModel) == null)
            return;

        (BindingContext as CatalogTabViewModel).IsRefreshing = false;


        if (searching)
            return;

        searching = true;

        (BindingContext as CatalogTabViewModel).SearchItems();

        await Task.Delay(300);

        searching = false;

    }
}