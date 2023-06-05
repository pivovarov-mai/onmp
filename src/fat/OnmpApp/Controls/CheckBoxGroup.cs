using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.Controls;

public class CheckBoxGroup : StackLayout
{
    public static readonly BindableProperty ItemsSourceProperty = BindableProperty.Create(nameof(ItemsSource), typeof(IList<string>), typeof(CheckBoxGroup), propertyChanged: (bindable, oldValue, newValue) =>
    {
        ((CheckBoxGroup)bindable).OnItemsSourceChanged(bindable, oldValue, newValue);
    });
    public static readonly BindableProperty SelectedOptionsProperty = BindableProperty.Create(nameof(SelectedOptions), typeof(IList<bool>), typeof(CheckBoxGroup), defaultBindingMode: BindingMode.TwoWay);

    public IList<string> ItemsSource
    {
        get => (IList<string>)GetValue(ItemsSourceProperty);
        set => SetValue(ItemsSourceProperty, value);
    }

    public IList<bool> SelectedOptions
    {
        get => (IList<bool>)GetValue(SelectedOptionsProperty);
        set => SetValue(SelectedOptionsProperty, value);
    }

    private void OnItemsSourceChanged(BindableObject bindable, object _, object newValue)
    {
        if (newValue is IList<string> items)
        {
            var checkBoxGroup = (CheckBoxGroup)bindable;
            checkBoxGroup.Children.Clear();

            for (int i = 0; i < items.Count; i++)
            {
                var checkBox = new CheckBox { IsChecked = SelectedOptions[i] };
                var label = new Label { Text = items[i], VerticalOptions = LayoutOptions.Center, FontFamily = "Arial", FontSize = 18 };

                checkBoxGroup.Children.Add(new StackLayout
                {
                    Orientation = StackOrientation.Horizontal,
                    Children = { checkBox, label }
                });

                int index = i;
                checkBox.CheckedChanged += (s, e) =>
                {
                    checkBoxGroup.SelectedOptions[index] = e.Value;
                };
            }
        }
    }
}