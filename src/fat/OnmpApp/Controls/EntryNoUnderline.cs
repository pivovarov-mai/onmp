namespace OnmpApp.Controls;

// Поле типа "Entry", но без нижней линии
public class EntryNoUnderline :Entry
{
    public static readonly BindableProperty NoUnderlineProperty =
        BindableProperty.Create(nameof(NoUnderline), typeof(bool), typeof(EntryNoUnderline), false);

    public bool NoUnderline
    {
        get => true;
        set => SetValue(NoUnderlineProperty, value);
    }
}
