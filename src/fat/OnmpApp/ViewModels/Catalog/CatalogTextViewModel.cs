using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using OnmpApp.Database;
using OnmpApp.Services;

namespace OnmpApp.ViewModels.Catalog;

[QueryProperty(nameof(Name), nameof(Name))]
public partial class CatalogTextViewModel : ObservableObject
{
    [ObservableProperty]
    Models.Database.Catalog _catalogElement = new();

    [ObservableProperty]
    string _name;

    [RelayCommand]
    async void ReloadCatalog()
    {
        CatalogElement = await CatalogService.Get(Name, true);
    }

    public async void InitPage()
    {
        CatalogElement = await CatalogService.Get(Name);
    }

}