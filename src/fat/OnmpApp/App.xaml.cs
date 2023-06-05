using Microsoft.Maui.Controls.Platform;
using OnmpApp.Controls;
using System.Globalization;

namespace OnmpApp;

public partial class App : Application
{
	public App()
	{
		InitializeComponent();

        MainPage = new AppShell();
		ModifyEntryWithoutUnderline();
		ModifyPickerWithoutUnderline();
		ModifyEditorWithoutUnderline();

	}

	static void ModifyEntryWithoutUnderline()
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

    static void ModifyPickerWithoutUnderline()
	{
		Microsoft.Maui.Handlers.PickerHandler.Mapper.AppendToMapping("NoUnderline", (h, v) =>
		{
			if (v is PickerNoUnderline)
			{
#if ANDROID
                Android.Graphics.Drawables.GradientDrawable gd = new();  
				gd.SetColor(global::Android.Graphics.Color.Transparent);  
				h.PlatformView.SetBackground(gd);  
#endif
			}
		});
	}
    static void ModifyEditorWithoutUnderline()
	{
		/*Microsoft.Maui.Handlers.EditorHandler.Mapper.AppendToMapping("NoUnderline", (h, v) =>
		{
			if (v is EditorNoUnderline)
			{
#if ANDROID
				GradientDrawable gd = new GradientDrawable();  
				gd.SetColor(global::Android.Graphics.Color.Transparent);  
				h.PlatformView.SetBackground(gd);  
#endif
			}
		});*/
	}

}
