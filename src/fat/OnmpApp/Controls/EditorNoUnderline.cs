using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.Controls;

public class EditorNoUnderline :Editor
{
    public static readonly BindableProperty NoUnderlineProperty =
        BindableProperty.Create(nameof(NoUnderline), typeof(bool), typeof(EditorNoUnderline), false);

    public bool NoUnderline
    {
        get => true;
        set => SetValue(NoUnderlineProperty, value);
    }
}
