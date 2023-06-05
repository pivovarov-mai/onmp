using CommunityToolkit.Maui.Core.Extensions;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using OnmpApp.Models;
using OnmpApp.Properties;
using OnmpApp.Services;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

using OnmpApp.Helpers;
using OnmpApp.Views.CardFiller;
using OnmpApp.Models.Database;

namespace OnmpApp.ViewModels.CardFiller;

[QueryProperty(nameof(CardId), nameof(CardId))]
public partial class EditorPreviewCardViewModel : ObservableObject
{
    
    [ObservableProperty] // Список шаблонов
    ObservableCollection<Card> _templates = new();
    [ObservableProperty] // Выбранный шаблон
    Card _selectedTemplate;

    [ObservableProperty]
    int _cardId = -1; // Id изменяемой карточки
    int _prevCardId = -1;

    [ObservableProperty]
    Card _card = new(); // Карточка

    [ObservableProperty]
    TimeSpan _time;

    [ObservableProperty]
    [NotifyPropertyChangedFor(nameof(NewCard))]
    bool _oldCard = false; // Была ли уже создана карта

    public bool NewCard => !OldCard;

    public IList<string> CardStatuses { get; } = Enum.GetValues(typeof(CardStatus))
                                                    .Cast<CardStatus>()
                                                    .Select(e => e.GetDescription())
                                                    .ToList();

    private string _selectedStatus;
    public string SelectedStatus
    {
        get => _selectedStatus;
        set
        {
            _selectedStatus = value;
            Card.Status = StringHelper.GetEnumFromDescription(value);
            OnPropertyChanged(nameof(SelectedStatus));
        }
    }

    public EditorPreviewCardViewModel() {
        SelectedStatus = CardStatuses[0];
    }

    [RelayCommand]
    async void PrintCard()
    {

    }

    public async Task<bool> GetTemplates()
    {
        var res = await CardService.Search("", false, false, true, false, -1, -1);
        Templates = res.OrderBy(el => el.Name).ToObservableCollection();
        Templates.Insert(0, new Card { Id = -1, Name = "Без шаблона"});
        SelectedTemplate = Templates[0];
        return true;
    }

    async Task<bool> Save()
    {
        if (string.IsNullOrWhiteSpace(Card.Name))
        {
            ToastHelper.Show("Имя не должно быть пустым");
            return false;
        }

        if (string.IsNullOrWhiteSpace(Card.Order))
        {
            ToastHelper.Show("Номер наряда не должен быть пустым");
            return false;
        }

        Card.Date = Card.Date.Date + Time;
        if (OldCard)
            await CardService.Update(Card);
        else
            await CardService.Insert(Card);

        return true;
    }

    bool _navigating = false;

    [RelayCommand]
    async void ContinueButton()
    {
        if (_navigating)
            return;

        _navigating = true;

        if (!await Save())
        {
            _navigating = false;
            return;
        }

        _prevCardId = Card.Id;
        if (!OldCard && SelectedTemplate.Id != -1)
            await Shell.Current.GoToAsync($"{nameof(EditorPreviewCardPage)}/{nameof(TemplateFillerPage)}?CardId={Card.Id}&TemplateId={SelectedTemplate.Id}", animate: true);
        else 
            await Shell.Current.GoToAsync($"{nameof(EditorPreviewCardPage)}/{nameof(TemplateFillerPage)}?CardId={Card.Id}", animate: true);

        _navigating = false;
    }

    [RelayCommand]
    async void SaveButton()
    {
        if (_navigating)
            return;

        _navigating = true;

        if (!await Save())
        {
            _navigating = false;
            return;
        }

        _prevCardId = -1;
        await Shell.Current.GoToAsync("..", animate: true);
        _navigating = false;
    }

    public async void InitCard()
    {


        if (CardId != -1 || _prevCardId != -1)
        {
            if(_prevCardId != -1)
                CardId = _prevCardId;

            OldCard = true;
            var card = await CardService.Get(CardId);
            Time = card.Date.TimeOfDay;
            Card = card;
            SelectedStatus = Card.Status.GetDescription();
        }
        else
        {
            OldCard = false;
            var card = new Card()
            {
                UserId = Settings.UserId,
                Status = CardStatus.Draft,
                Order = await CardService.GetLastOrder(),
            };

            Time = card.Date.TimeOfDay;
            Card = card;
            SelectedStatus = CardStatuses[0];
            _ = await GetTemplates();

        }

    }
}
