using OnmpApp.Controls;

namespace OnmpApp;

public partial class App : Application
{
	public App()
	{
		InitializeComponent();

		MainPage = new AppShell();
		ModifyEntryWithoutUnderline();
	}

	void ModifyEntryWithoutUnderline()
	{
        Microsoft.Maui.Handlers.EntryHandler.Mapper.AppendToMapping("NoUnderline", (h, v) =>
        {
			if (v is EntryNoUnderline)
			{
#if ANDROID
				h.PlatformView.BackgroundTintList = Android.Content.Res.ColorStateList.ValueOf(Android.Graphics.Color.Transparent) ;
#endif
#if IOS
				// TODO: убрать нижнюю границу в Entry в IOS
				// h.PlatformView.BorderStyle = UIKit.UITextBorderStyle.None;
#endif
			}
        });
    }
}
