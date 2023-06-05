using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using SQLite;


namespace OnmpApp.Models.Database;

[Table("FullCards")]
public class FullCard
{
    [PrimaryKey]
    public int Id { get; set; }

    [TextQuestion("Жалобы")]
    public string Complaints { get; set; }

    [TextQuestion("Анамнез")]
    public string Anamnesis { get; set; }

    [RadioButtonQuestion("Общее состояние", new string[] { "удовл.", "ср. тяжести", "тяжелое", "терминальное" })]
    public string GeneralState { get; set; }

    [RadioButtonWithTextQuestion("Сознание", new string[] { "ясное", "оглушенное", "сопор", "кома" })]
    public string Consciousness { get; set; }

    [RadioButtonWithTextQuestion("Положение", new string[] { "активное", "пассивное", "вынужденное" })]
    public string Position { get; set; }

    [CheckBoxWithTextQuestion("Кожные покровы", new string[] { "сухие", "влажные", "обычной окраски", "бледные", "гиперемия", "цианоз", "желтушность" })]
    public string Skin { get; set; }

    [RadioButtonWithTextQuestion("Сыпь", new string[] { "нет" })]
    public string Rash { get; set; }

    [RadioButtonWithTextQuestion("Зев", new string[] { "чистый" })]
    public string Zev { get; set; }

    [RadioButtonWithTextQuestion("Миндалины", new string[] { "не увеличены" })]
    public string Tonsils { get; set; }

    [RadioButtonWithTextQuestion("Лимфоузлы", new string[] { "не увеличены" })]
    public string LymphNodes { get; set; }

    [RadioButtonWithTextQuestion("Пролежни", new string[] { "нет" })]
    public string Bedsores { get; set; }

    [RadioButtonWithTextQuestion("Отеки", new string[] { "нет" })]
    public string Edema { get; set; }

    [TextQuestion("Температура", typeof(double))]
    public double Temperature { get; set; }

    [TextQuestion("ЧДД", typeof(int))]
    public int RespiratoryRate { get; set; }

    [RadioButtonQuestion("Одышка", new string[] { "эксператорная", "инспираторная", "смешанная" })]
    public string Dyspnea { get; set; }

    [RadioButtonQuestion("Патологическое дыхание", new string[] { "нет", "Чейна-Стокса", "Биотта", "Куссмауля", "брадипноэ", "гиперпноэ", "тахипноэ", "шумное дыхание" })]
    public string PathologicalBreathing { get; set; }

    [CheckBoxWithTextQuestion("Аускультативно", new string[] { "везикулярное", "жесткое", "бронхиальное", "пуэрильное", "ослаблено", "отсутствует" }, "в")]
    public string Auscultatory { get; set; }

    [RadioButtonQuestion("Хрипы", new string[] { "сухие", "Влажные" })]
    public string Wheezing { get; set; }

    [CheckBoxWithTextQuestion("Сухие", new string[] { "свистящие", "жужжащие" }, "в")]
    public string Dry { get; set; }

    [CheckBoxWithTextQuestion("Влажные", new string[] { "мелко-", "средне-", "крупнопузырчатые" }, "в")]
    public string Wet { get; set; }

    [CheckBoxWithTextQuestion("", new string[] { "Крепитация", "шум трения плевры" }, "над")]
    public string Crepitus { get; set; }

    [CheckBoxWithTextQuestion("Перкуторный звук", new string[] { "легочный", "тимпанический", "коробочный", "притупленный", "тупой" }, "над")]
    public string PercussionSound { get; set; }

    [CheckBoxQuestion("Кашель", new string[] { "сухой", "влажный", "лающий", "отсутствует" })]
    public string Cough { get;set; }

    [RadioButtonWithTextQuestion("Мокрота", new string[] { "нет" })]
    public string Sputum { get; set; }

    [TextQuestion("Пульс", typeof(int))]
    public int Pulse { get; set; }

    [RadioButtonQuestion("", new string[] { "ритмичный", "аритмичный" })]
    public string Rhytmic { get; set; }

    [RadioButtonQuestion("Наполнение", new string[] { "удовлетворительное", "слабое", "не определено" })]
    public string Filling { get; set; }

    [TextQuestion("ЧСС", typeof(int))]
    public int HeartRate { get; set; }

    [TextQuestion("Дефицит пульса", typeof(int))]
    public int PulseDeficit { get; set; }

    [TextQuestion("АД")]
    public string ArterialPressure { get; set; }

    [TextQuestion("Привычное")]
    public string Habitual { get; set; }

    [TextQuestion("Максимальное")]
    public string Maximum { get; set; }

    [RadioButtonQuestion("Тоны сердца", new string[] { "звучные", "приглушены", "глухие" })]
    public string HeartSounds { get; set; }

    [CheckBoxWithTextQuestion("Шум", new string[] { "систолический", "диастолический", "нет" }, "на")]
    public string NoiseSystolic { get; set; }

    [RadioButtonWithTextQuestion("Проводится", new string[] { "нет" })]
    public string Held { get;set; }

    [RadioButtonQuestion("", new string[] { "Шум трения перикарда", "нет" })]
    public string Shum { get; set; }

    [RadioButtonWithTextQuestion("Акцент тона", new string[] { "I", "II" }, "на")]
    public string Accent { get; set; }

    [RadioButtonQuestion("Язык", new string[] { "сухой", "влажный" })]
    public string Tongue { get; set; }

    [RadioButtonWithTextQuestion("Обложен", new string[] { "девиация языка влево", "девиация языка право", "расположен по средней линии", "резкий запах алкоголя изо рта", "резкий запах ацетона", "следы прикуса языка" })]
    public string Oblojen { get; set; }

    [RadioButtonQuestion("Форма живота", new string[] { "правильная", "увеличен", "ассиметричен" })]
    public string Belly { get; set; }

    [RadioButtonWithTextQuestion("", new string[] { "мягкий", "напряжен" }, "в")]
    public string Tense { get; set; }

    [RadioButtonWithTextQuestion("", new string[] { "безболезненный", "болезненный" }, "в")]
    public string Painful { get; set; }

    [RadioButtonWithTextQuestion("Положительные симптомы", new string[] { "Образцова", "Ровзинга", "Ситковского", "Ортнера", "Мерфи", "Мейо-Робсона", "Щеткина-Блюмберга", "Вааля", "отрицательные" })]
    public string PositiveSymptoms { get; set; }

    [RadioButtonWithTextQuestion("Перистальтика", new string[] { "выслушивается", "усиленная", "не выслушивается" })]
    public string Peristalsis { get; set; }

    [RadioButtonWithTextQuestion("Печень", new string[] { "не увеличена", "по краю реберной дуги" })]
    public string Liver { get;set; }

    [RadioButtonWithTextQuestion("Селезенка", new string[] { "не пальпируется" })]
    public string Spleen { get; set; }

    [RadioButtonWithTextQuestion("Рвота (частота)", new string[] { "нет" })]
    public string Vomit { get; set; }

    [RadioButtonWithTextQuestion("Стул (консистенация, частота)", new string[] { "регулярный", "оформлен" })]
    public string Feces { get; set; }

    [CheckBoxQuestion("Поведение", new string[] { "спокойное", "беспокойное", "возбужден" })]
    public string Behavior { get; set; }

    [RadioButtonWithTextQuestion("Контакт", new string[] { "контактен" })]
    public string Contact { get; set; }

    [RadioButtonQuestion("Чувствительность", new string[] { "сохранена D = S", "D > S", "D < S" })]
    public string Sensitivity { get; set; }

    [RadioButtonWithTextQuestion("Речь", new string[] { "внятная", "дизартрия", "афазия" })]
    public string Speech { get; set; }

    [RadioButtonQuestion("Зрачки", new string[] { "OD = OS", "OD > OS", "OD < OS" })]
    public string Pupils { get; set; }

    [RadioButtonQuestion("", new string[] { "обычные", "широкие", "узкие" })]
    public string Pupils2 { get; set; }

    [RadioButtonWithTextQuestion("Фотореакция", new string[] { "живая" })]
    public string Photoreaction { get; set; }

    [RadioButtonWithTextQuestion("Нистагм", new string[] { "нет", "мелкоразмашистый", "крупноразмашистый", "влево", "вправо", "при взгляде в сторону" })]
    public string Nystagmus { get; set; }

    [RadioButtonWithTextQuestion("Ассиметрия лица", new string[] { "нет", "сглаженность носогубной складки", "справа", "слева" })]
    public string FacialAsymmentry { get; set; }

    [RadioButtonWithTextQuestion("Менингиальные симптомы", new string[] { "ригидность затылочных мышц", "Кенига", "Брудзинского" })]
    public string MeningealSymptoms { get; set; }

    [TextQuestion("Очаговые симптомы")]
    public string FocalSymptoms { get; set; }

    [RadioButtonWithTextQuestion("Координатные пробы", new string[] { "в позе Ромберга", "устойчив", "неустойчив", "пальценосовая проба", "коленнопяточная проба", "выполняет правильно", "промахивается", "справа", "слева" })]
    public string CoordinatorSamples { get; set; }

    [RadioButtonWithTextQuestion("Мочеполовая система", new string[] { "дизурии нет", "дизурических расстройств нет, моча светло-желтого цвета", "дизурических расстройств не выявлено, моча желтого цвета", "следы непроизвольного мочеиспускания", "задержка мочеиспускания в течении ", "мочевой пузырь увеличен и выступает над лоном на ", "симметричен, болезнен при пальпации", "частое, болезненное мочеиспускание, моча темно-желтого цвета без примесей", "частое, безболезненное мочеиспускание, моча темно-желтого цвета без примесей, ложные порывы", "болезненное мочеиспускание, моча мутная с белыми хлопьями", "безболезненное мочеиспукание, моча мутная с белыми хлопьями", "безболезненное мочеиспускание, моча темно-красного цвета со сгустками", "безболезненное мочеиспускание, моча темно-красного цвета", "неизвестно", "мочется в памперс" })]
    public string GenitourinarySystem { get; set; }

    [RadioButtonWithTextQuestion("Симптомы поколачивания", new string[] { "отрицательный с обеих сторон", "положительный", "справа", "слева" })]
    public string TappingSymptom { get; set; }

    [TextQuestion("Вес", typeof(double))]
    public double Weight { get; set; }

    [TextQuestion("Рост", typeof(double))]
    public double Height { get; set; }

    [TextQuestion("Status localis")]
    public string StatusLocalis { get; set; }

    [TextQuestion("Глюкометрия")]
    public string GlukoMetria { get; set; }

    [TextQuestion("SpO^2")]
    public string SpOTwo { get; set; }

    [TextQuestion("ЭКГ")]
    public string EKG { get; set; }

    [RadioButtonWithTextQuestion("Оказанная помощь и ее эффект", new string[] { "расспрос", "изучение архива ЭКГ", "изучение мед. документов", "физические методы охлаждения" })]
    public string Assistance { get; set; }

    [RadioButtonWithTextQuestion("Медикаменты", new string[] { "Sol.Analgini 500mg/ml-2ml", "Sol.Ketaroli 30mg/ml-1ml", "Sol.Drotaverini 20mg/ml-2ml", "Sol.Medopredi 30mg/ml-1ml", "Sol.Prednizoloni 30mg/ml-1ml", "Sol. Dexametazoni 4mg/ml-1ml", "Sol.Chloropyramini 20mg/ml-1ml", "Sol.Spasmalini 5ml", "Sol.Metoclopramidi 5mg/ml-2ml", "Sol.Magnesii sulfatis 250mg/ml-10ml", "Sol.Ebrantili 5mg/ml-5ml", "Sol.Betaloci 1mg/ml-5ml", "Sol.Natrii chloridi 0,9%-10ml", "Sol.Natrii chloridi 0,9%-250ml", "Sol.Glucosae 40%-10ml", "Sol.Beroduali 20ml", "Pulmicort susp.0,5mg/ml-2ml", "Tab.Paracetamoli 500mg", "Tab.Captoprili 25mg", "Tab.Moxonidini 0,4mg", "Tab. Glicini 500mg", "Tab.Carbonii activatis 250mg", "Tab.Acidi acetylsalicylici 500 mg", "в/м в правую ягодичную область", "в/в медленно под контролем АД в течении 3 минут введено" })]
    public string Medicine { get; set; }

    [RadioButtonWithTextQuestion("Результат вызова", new string[] { "Оставлен на месте, рекомендовано обратиться в поликлинику", "Оставлен на месте, актив в поликлинику", "Вызов бригады СМП", "Отказ от вызова бригады СМП, актив ОНМП", "Отказ от вызова бригады СМП, актив в поликлинику", "Отказ от вызова бригады СМП, рекомендовано обратиться в поликлинику" })]
    public string Results { get; set; }

    [RadioButtonWithTextQuestion("Рекомендации", new string[] { "Ведение дневника контроля АД", "Регулярный прием базовой антигипертензивной терапии" })]
    public string Recomendations { get; set; }

    [TextQuestion("Оценка эффекта")]
    public string Ocenka { get; set; }

    /*
       
        [ButtonQuestion("Сигнальная карта", new string[] {"нет"})]
        my_form_rashod(array("Салфетки","Бахилы","Перчатки","Маска","Шпатель","Чехол (град)","Шприц 2,0","Шприц 5,0","Шприц 10,0","Шприц 20,0","Катетер","Пластырь","Скариф","Полоски","Пакет","Маска (неб)"))

        */
}
