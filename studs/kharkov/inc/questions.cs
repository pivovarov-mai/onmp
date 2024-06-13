public class FullCard
{
    [TextQuestion("Жалобы")]
    public string Complaints { get; set; }
    [RadioButtonQuestion("Общее состояние", new string[] { "удовл.", "ср. тяжести", "тяжелое", "терминальное" })]
    public string GeneralState { get; set; }
    [RadioButtonWithTextQuestion("Сознание", new string[] { "ясное", "оглушенное", "сопор", "кома" })]
    public string Consciousness { get; set; }

    // Остальные поля
}