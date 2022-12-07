namespace OnmpApp.Controls;

public class EntryNoUnderline :Entry
{
    public static readonly BindableProperty NoUnderlineProperty =
        BindableProperty.Create("NoUnderline", typeof(bool), typeof(EntryNoUnderline), false);

    public bool NoUnderline
    {
        get => true;
        set => SetValue(NoUnderlineProperty, value);
    }
}
