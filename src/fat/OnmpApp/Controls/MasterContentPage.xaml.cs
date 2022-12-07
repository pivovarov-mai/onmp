using CommunityToolkit.Mvvm.Input;
using System.ComponentModel;

namespace OnmpApp.Controls;

public partial class MasterContentPage : ContentPage, INotifyPropertyChanged
{
	public MasterContentPage()
	{
		InitializeComponent();
	}

	[RelayCommand]
	async Task GoBack()
	{
		await Shell.Current.GoToAsync("..", animate: true);
	}


	// Видимость кнопки "Назад"
	public static readonly BindableProperty BackButtonVisibleProperty = BindableProperty.Create(propertyName: nameof(BackButtonVisible), 
		returnType: typeof(bool), declaringType: typeof(MasterContentPage), defaultValue: false);

	public bool BackButtonVisible
	{
		get => (bool)GetValue(BackButtonVisibleProperty);
		set => SetValue(BackButtonVisibleProperty, value);
	}

    // Текст заголовка
    public static readonly BindableProperty HeaderTextProperty = BindableProperty.Create(propertyName: nameof(HeaderText),
        returnType: typeof(string), declaringType: typeof(MasterContentPage), defaultValue: "");

    public string HeaderText
    {
        get => (string)GetValue(HeaderTextProperty);
        set => SetValue(HeaderTextProperty, value);
    }


    // Видимость правой кнопки
    public static readonly BindableProperty RightButtonVisibleProperty = BindableProperty.Create(propertyName: nameof(RightButtonVisible),
        returnType: typeof(bool), declaringType: typeof(MasterContentPage), defaultValue: false);

    public bool RightButtonVisible
    {
        get => (bool)GetValue(RightButtonVisibleProperty);
        set => SetValue(RightButtonVisibleProperty, value);
    }

    // Изображение правой кнопки
    public static readonly BindableProperty RightButtonSourceProperty = BindableProperty.Create(propertyName: nameof(RightButtonSource),
        returnType: typeof(object), declaringType: typeof(MasterContentPage), defaultValue: null);

    public object RightButtonSource
    {
        get => (object)GetValue(RightButtonSourceProperty);
        set => SetValue(RightButtonSourceProperty, value);
    }

    // Действие правой кнопки
    public static readonly BindableProperty RightButtonCommandProperty = BindableProperty.Create(propertyName: nameof(RightButtonCommand),
        returnType: typeof(object), declaringType: typeof(MasterContentPage), defaultValue: null);

    public object RightButtonCommand
    {
        get => (object)GetValue(RightButtonCommandProperty);
        set => SetValue(RightButtonCommandProperty, value);
    }

}