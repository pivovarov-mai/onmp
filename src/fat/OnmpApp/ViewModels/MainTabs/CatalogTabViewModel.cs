using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CommunityToolkit.Maui.Core.Extensions;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using OnmpApp.Database;
using OnmpApp.Models.Database;
using OnmpApp.Services;
using OnmpApp.ViewModels.Catalog;
using OnmpApp.Views.Catalog;

namespace OnmpApp.ViewModels.MainTabs;
public partial class CatalogTabViewModel : ObservableObject
{
    [ObservableProperty]
    string _searchText = "";

    [ObservableProperty]
    ObservableCollection<CatalogShort> _catalogElements = new();


    [ObservableProperty]
    bool _isRefreshing = false;

    public CatalogTabViewModel()
    {

    }

    bool _searching = false;

    [RelayCommand] // Добавление элементов, которые не были показаны
    async void RemainingItemsThresholdReached()
    {
        if (_searching) return;

        _searching = true;

        var res = await CatalogService.Search(SearchText, CatalogElements.Count);
        foreach(var item in res)
        {
            CatalogElements.Add(item);
        }

        _searching = false;
    }

    public async void SearchItems()
    {
        IsRefreshing = true;

        if (_searching) return;

        _searching = true;


        var res = await CatalogService.Search(SearchText);
        CatalogElements = res?.ToObservableCollection();

        IsRefreshing = false;

        _searching = false;
    }

    [RelayCommand] // Нажатие на карту
    async void ItemTapped(CatalogShort selectedCatalog)
    {
        if (selectedCatalog == null)
            return;

        await Shell.Current.GoToAsync($"{nameof(CatalogTextPage)}?Name={selectedCatalog.Name}", animate: true);
    }

    

}
