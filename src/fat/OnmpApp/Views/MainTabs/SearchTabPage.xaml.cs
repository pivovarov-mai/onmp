using System.Threading;
using OnmpApp.Controls;
using OnmpApp.Models;
using OnmpApp.Models.Database;
using OnmpApp.ViewModels.MainTabs;

namespace OnmpApp.Views.MainTabs;

public partial class SearchTabPage : MasterContentPage
{
	public SearchTabPage(SearchTabViewModel _vm)
	{
		InitializeComponent();
		BindingContext = _vm;
	}

	private void OnDeleteSwipeItemInvoked(object sender, EventArgs e)
	{
		if ((BindingContext as SearchTabViewModel) == null)
			return;

		var swipeItemView = (SwipeItem)sender;
		var smallCard = (Card)swipeItemView.BindingContext;

        (BindingContext as SearchTabViewModel).ItemDelete(smallCard);
	}

	private void OnArchiveSwipeItemInvoked(object sender, EventArgs e)
	{
		if ((BindingContext as SearchTabViewModel) == null)
			return;

		var swipeItemView = (SwipeItem)sender;
		var smallCard = (Card)swipeItemView.BindingContext;

        (BindingContext as SearchTabViewModel).ItemArchive(smallCard);
	}

    bool searching = false;

    private async void SearchChanged(object sender, EventArgs e)
	{
		if ((BindingContext as SearchTabViewModel) == null)
			return;

        (BindingContext as SearchTabViewModel).IsRefreshing = false;


        if (searching)
			return;

		searching = true;

        (BindingContext as SearchTabViewModel).SearchNewItems();

        await Task.Delay(300);

        searching = false;

    }
}