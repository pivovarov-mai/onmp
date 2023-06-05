using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using OnmpApp.Models;
using OnmpApp.Models.Database;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OnmpApp.Database;
using OnmpApp.Services;
using CommunityToolkit.Maui.Core.Extensions;

namespace OnmpApp.ViewModels.CardFiller;

[QueryProperty(nameof(CardId), nameof(CardId))]
[QueryProperty(nameof(TemplateId), nameof(TemplateId))]
public partial class TemplateFillerViewModel : ObservableObject
{
    [ObservableProperty]
    ObservableCollection<Question> _questions = null;

    [ObservableProperty]
    bool _isFinishButtonVisible = false;

    [ObservableProperty]
    int _cardId = -1;

    int _prevCardId = -1;

    [ObservableProperty]
    int _templateId = -1;

    [ObservableProperty]
    FullCard _card = new FullCard();



    public TemplateFillerViewModel()
    {
        
    }

    public async void InitCard()
    {
        if(_prevCardId == CardId) return;

        Card = await FullCardService.Get(CardId);

        if(TemplateId > 0)
        {
            var card = await FullCardService.Get(TemplateId);
            card.Id = CardId;
            Card = card;
            await FullCardService.Update(Card);
        }

        Questions = TestQuestionsFactory.CreateFromAttributes(Card).ToObservableCollection();
        _prevCardId = CardId;
    }

    private void SaveTestResults(FullCard fullCard)
    {
        if (fullCard == null) throw new ArgumentNullException(nameof(fullCard));

        var properties = typeof(FullCard).GetProperties();

        for (int i = 0; i < Questions.Count; i++)
        {
            var property = properties[i+1];
            var question = Questions[i];

            if (property.PropertyType == typeof(int) || property.PropertyType == typeof(double))
            {
                if(property.PropertyType == typeof(int) && int.TryParse(question.GetValue(), out int res1))
                    property.SetValue(fullCard, res1);
                else if (property.PropertyType == typeof(double) && double.TryParse(question.GetValue().Replace('.', ','), out double res2))
                    property.SetValue(fullCard, res2);
                else
                    property.SetValue(fullCard, 0);
            }
            else
            {
                property.SetValue(fullCard, question.GetValue());
            }

        }
    }


    bool _navigating = false;
    [RelayCommand]
    async void ButtonPressed()
    {
        if (_navigating) return;

        _navigating = true;
        SaveTestResults(Card);
        await FullCardService.Update(Card);
        await Shell.Current.GoToAsync("../..", animate: true);

        _navigating = false;
    }

}
