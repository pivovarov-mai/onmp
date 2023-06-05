using System.ComponentModel;

namespace OnmpApp.Behaviors;

// Анимация "появления" при выходе из невидимости элементов
public class VisibilityAnimationBehavior : Behavior<View>
{
    // Поле для элементов, которые также должны быть с анимацией, но всегда видимы
    public static readonly BindableProperty TranslateAnimationProperty =
        BindableProperty.Create(nameof(TranslateAnimation), typeof(bool), typeof(VisibilityAnimationBehavior),
            default(bool));

    private View _associatedObject;

    public bool TranslateAnimation
    {
        get => (bool)GetValue(TranslateAnimationProperty);
        set => SetValue(TranslateAnimationProperty, value);
    }

    protected override void OnAttachedTo(View bindable)
    {
        _associatedObject = bindable;
        base.OnAttachedTo(bindable);
        bindable.PropertyChanged += OnViewPropertyChanged;
    }

    protected override void OnDetachingFrom(View bindable)
    {
        base.OnDetachingFrom(bindable);
        bindable.PropertyChanged -= OnViewPropertyChanged;
    }

    private async void OnViewPropertyChanged(object sender, PropertyChangedEventArgs e)
    {
        if (e.PropertyName == nameof(View.IsVisible))
        {
            if (_associatedObject.IsVisible)
                await ShowViewAsync();
            else
                await HideViewAsync();
        }
    }

    private async Task ShowViewAsync()
    {
        await Task.WhenAll(
            _associatedObject.FadeTo(1),
            TranslateAnimation ? _associatedObject.TranslateTo(0, 0) : Task.CompletedTask
        );
    }

    private async Task HideViewAsync()
    {
        await Task.WhenAll(
            _associatedObject.FadeTo(0),
            TranslateAnimation ? _associatedObject.TranslateTo(0, -20) : Task.CompletedTask
        );
    }
}