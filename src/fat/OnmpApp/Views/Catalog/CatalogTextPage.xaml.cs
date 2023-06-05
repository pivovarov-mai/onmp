using OnmpApp.Controls;
using OnmpApp.ViewModels.Catalog;

namespace OnmpApp.Views.Catalog;

public partial class CatalogTextPage : MasterContentPage
{
	public CatalogTextPage(CatalogTextViewModel vm)
	{
		InitializeComponent();
        BindingContext = vm;
    }

    private void CatalogTextPage_OnAppearing(object sender, EventArgs e)
    {
        if ((BindingContext as CatalogTextViewModel) == null)
            return;

        (BindingContext as CatalogTextViewModel).InitPage();
    }
}