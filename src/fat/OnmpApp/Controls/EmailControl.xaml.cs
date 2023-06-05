namespace OnmpApp.Controls;

// Поле для ввода почты
public partial class EmailControl : ContentView
{

	public EmailControl()
	{
		InitializeComponent();
	}

	// Название над полем
	public static readonly BindableProperty LabelTextProperty = BindableProperty.Create(propertyName: nameof(LabelText),
		returnType: typeof(string), declaringType: typeof(EmailControl), defaultValue: "", defaultBindingMode: BindingMode.TwoWay);

	public string LabelText
	{
		get => (string)GetValue(LabelTextProperty);
		set => SetValue(LabelTextProperty, value);
	}

	// Текст в поле
	public static readonly BindableProperty EntryTextProperty = BindableProperty.Create(propertyName: nameof(EntryText),
		returnType: typeof(string), declaringType: typeof(EmailControl), defaultValue: "", defaultBindingMode: BindingMode.TwoWay);

	public string EntryText
	{
		get => (string)GetValue(EntryTextProperty);
		set => SetValue(EntryTextProperty, value);
	}

	// Триггер для действия при ошибке
	public static readonly BindableProperty InvalidTrigerProperty = BindableProperty.Create(propertyName: nameof(InvalidTriger),
		returnType: typeof(bool), declaringType: typeof(EmailControl), defaultValue: false, defaultBindingMode: BindingMode.TwoWay);

	public bool InvalidTriger
	{
		get => (bool)GetValue(InvalidTrigerProperty);
		set => SetValue(InvalidTrigerProperty, value);
	}
}