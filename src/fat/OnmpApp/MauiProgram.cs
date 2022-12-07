using Microsoft.Extensions.Logging;
using OnmpApp.ViewModels;
using OnmpApp.Views;
using CommunityToolkit.Maui;
using OnmpApp.Data;

namespace OnmpApp;

public static class MauiProgram
{
	public static MauiApp CreateMauiApp()
	{
		var builder = MauiApp.CreateBuilder();
		builder
			.UseMauiApp<App>()
			.ConfigureFonts(fonts =>
			{
				fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
				fonts.AddFont("OpenSans-Semibold.ttf", "OpenSansSemibold");
			}).UseMauiCommunityToolkit()
			.RegisterViewModels()
			.RegisterViews();

#if DEBUG
		builder.Logging.AddDebug();
#endif

		_ = Database.Init();

        return builder.Build();
	}

	public static MauiAppBuilder RegisterViewModels(this MauiAppBuilder mauiAppBuilder)
	{
        mauiAppBuilder.Services.AddTransient<ViewModels.Authorize.LoginViewModel>();
        mauiAppBuilder.Services.AddTransient<ViewModels.Authorize.RegistrationViewModel>();

        mauiAppBuilder.Services.AddTransient<ViewModels.MainTabs.SearchTabViewModel>();

        mauiAppBuilder.Services.AddTransient<ViewModels.UserSettings.SettingsViewModel>();

        return mauiAppBuilder;
    }

	public static MauiAppBuilder RegisterViews(this MauiAppBuilder mauiAppBuilder)
	{
        mauiAppBuilder.Services.AddTransient<Views.Authorize.LoginPage>();
        mauiAppBuilder.Services.AddTransient<Views.Authorize.RegistrationPage>();

        mauiAppBuilder.Services.AddTransient<Views.MainTabs.SearchTabPage>();

        mauiAppBuilder.Services.AddTransient<Views.UserSettings.SettingsPage>();

        return mauiAppBuilder;
    }
}
