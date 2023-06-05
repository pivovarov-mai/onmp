using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using Newtonsoft.Json.Linq;
using OnmpApp.Models.Database;
using OnmpApp.Services;
using OnmpApp.Views.Authorize;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.ViewModels.UserSettings;

public partial class SettingsViewModel : ObservableObject
{

    [ObservableProperty]
    double _loaderProgress = 0;

    [ObservableProperty]
    bool _catalogLoading = false;

    [ObservableProperty]
    string _loaderText = $"Состояние загрузки: 0 %";

    [RelayCommand] // Загрузка справочника
    async Task LoadCatalog()
    {
        if (CatalogLoading)
            return;
        try
        {
            CatalogLoading = true;
            LoaderProgress = 0;
            LoaderText = $"Состояние загрузки: 0 %";

            await InitService.LoadCatalogNames();
            LoaderProgress = 0.05;
            int prevTextProgress = (int)(LoaderProgress * 100);
            LoaderText = $"Состояние загрузки: {prevTextProgress} %";

            int cnt = await CatalogService.Count();
            for (int i = 0; i < Enum.GetValues(typeof(CatalogType)).Length; i++)
            {
                dynamic json = JObject.Parse(await CatalogService.LoadData((CatalogType)i));
                foreach (dynamic item in json)
                {
                    if (item == null || item.Name == null || item.Value == null)
                        continue;

                    var catalog = await CatalogService.Get(item.Name.ToString());
                    catalog.Text = item.Value.ToString();
                    await CatalogService.Update(catalog);

                    LoaderProgress += 0.95 / cnt;
                    int textProgress = (int)(LoaderProgress * 100);
                    if (textProgress - prevTextProgress > 5)
                    {
                        LoaderText = $"Состояние загрузки: {textProgress} %";
                        prevTextProgress = textProgress;
                    }
                }
            }

            LoaderText = "Успешно загружено!";
        }
        catch (Exception)
        {
            CatalogLoading = false;
        }

        
    }



    [RelayCommand] // Выход из программы
    async Task LogOut()
    {
        Properties.Settings.WasAuthorized = false;
        Properties.Settings.Password = "";
        Properties.Settings.Token = "";
        await Shell.Current.GoToAsync($"//{nameof(LoginPage)}");
    }

    [ObservableProperty]
    string _currentVersion = AppInfo.Current.VersionString;
}
