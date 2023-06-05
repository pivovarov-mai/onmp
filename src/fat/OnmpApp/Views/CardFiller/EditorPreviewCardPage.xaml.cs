using OnmpApp.Controls;
using OnmpApp.ViewModels.CardFiller;

namespace OnmpApp.Views.CardFiller;

public partial class EditorPreviewCardPage : MasterContentPage
{
	public EditorPreviewCardPage(EditorPreviewCardViewModel vm)
	{
		InitializeComponent();
		BindingContext = vm;
	}

	private void MasterContentPage_Appearing(object sender, EventArgs e)
	{
		(BindingContext as EditorPreviewCardViewModel).InitCard();
	}
}