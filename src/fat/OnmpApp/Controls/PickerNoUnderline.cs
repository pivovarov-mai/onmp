using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.Controls;

// Поле типа Picker, но без нижней границы
public class PickerNoUnderline : Picker
{
    public static readonly BindableProperty NoUnderlineProperty =
        BindableProperty.Create(nameof(NoUnderline), typeof(bool), typeof(PickerNoUnderline), false);

    public bool NoUnderline
    {
        get => true;
        set => SetValue(NoUnderlineProperty, value);
    }
}
