namespace OnmpApp.Triggers;

// Анимация дрожания влево-вправо
public class WrongValsTriggerAction : TriggerAction<VisualElement>
{
    protected override async void Invoke(VisualElement sender)
    {
        int len = 10;
        uint time = 40;

        await sender.TranslateTo(-len, 0, time, Easing.Linear);
        for(int i = 0; i < 2; i++)
        {
            await sender.TranslateTo(len, 0, 2*time, Easing.Linear);
            await sender.TranslateTo(-len, 0, 2*time, Easing.Linear);
        }
        await sender.TranslateTo(len, 0, 2*time, Easing.Linear);
        await sender.TranslateTo(0, 0, time, Easing.Linear);
    }
}
