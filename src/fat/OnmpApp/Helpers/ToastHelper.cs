using CommunityToolkit.Maui.Alerts;
using CommunityToolkit.Maui.Core;

namespace OnmpApp.Helpers;

public static class ToastHelper
{
    // Небольшое всплывающее окно внизу приложения
    public static async void Show(string message, ToastDuration duration = ToastDuration.Short, 
        double fontSize = 14)
    {

        await Application.Current.MainPage.DisplayAlert("", message, "OK");
        /*CancellationTokenSource cancellationTokenSource = new();
        var toast = Toast.Make(message, duration, fontSize);
        await toast.Show(cancellationTokenSource.Token);*/
    }

}
