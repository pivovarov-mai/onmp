using OnmpApp.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.Controls;

public class RadioButtonGroup : StackLayout
{
    public RadioButtonGroup()
    {
        Orientation = StackOrientation.Vertical;
    }

    protected override void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        base.OnPropertyChanged(propertyName);

        if (propertyName == ItemsSourceProperty.PropertyName)
        {
            UpdateRadioButtons();
        }
        else if (propertyName == SelectedIndexProperty.PropertyName)
        {
            UpdateSelectedRadioButton();
        }
    }

    public static readonly BindableProperty ItemsSourceProperty = BindableProperty.Create(nameof(ItemsSource), typeof(IList<string>), typeof(RadioButtonGroup),
        default(IList<string>));

    public IList<string> ItemsSource
    {
        get => (IList<string>)GetValue(ItemsSourceProperty);
        set => SetValue(ItemsSourceProperty, value);
    }

    public static readonly BindableProperty SelectedIndexProperty = BindableProperty.Create(nameof(SelectedIndex), typeof(int), typeof(RadioButtonGroup), default(int));

    public int SelectedIndex
    {
        get => (int)GetValue(SelectedIndexProperty);
        set => SetValue(SelectedIndexProperty, value);
    }

    private void UpdateRadioButtons()
    {
        Children.Clear();

        if (ItemsSource == null)
        {
            return;
        }

        for (int i = 0; i < ItemsSource.Count; i++)
        {
            var radioButton = new RadioButton { Content = ItemsSource[i].ToString() };
            radioButton.CheckedChanged += OnRadioButtonChecked;
            Children.Add(radioButton);
        }

        if(SelectedIndex != -1)
            ((RadioButton)Children[SelectedIndex]).IsChecked = true;
    }

    private void UpdateSelectedRadioButton()
    {
        for (int i = 0; i < Children.Count; i++)
        {
            if (Children[i] is RadioButton radioButton)
            {
                radioButton.IsChecked = i == SelectedIndex;
            }
        }
    }

    public CollectionView ParentCarouselView { get; set; }

    private void OnRadioButtonChecked(object sender, CheckedChangedEventArgs e)
    {
        if (e.Value)
        {
            var selectedRadioButton = (RadioButton)sender;
            SelectedIndex = Children.IndexOf(selectedRadioButton);

            if (ParentCarouselView == null)
            {
                var parent = this.Parent;

                while (parent != null)
                {
                    if (parent is CollectionView carouselView)
                    {
                        ParentCarouselView = carouselView;
                        break;
                    }

                    parent = parent.Parent;
                }
            }

            // Если найден CarouselView, прокрутите к следующему элементу
            if (BindingContext is RadioButtonQuestion && BindingContext is not RadioButtonWithTextQuestion)
            {
                if (ParentCarouselView != null)
                {
                    var questionIndex = ParentCarouselView.ItemsSource.Cast<object>().ToList().IndexOf(BindingContext);

                    if (questionIndex >= 0 && questionIndex < ParentCarouselView.ItemsSource.Cast<object>().Count() - 1)
                    {
                        ParentCarouselView.ScrollTo(questionIndex + 1, position: ScrollToPosition.Center, animate: true);
                    }
                }
            }

        }
    }
}