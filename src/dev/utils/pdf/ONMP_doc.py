from lib import *

dct = {}
with open("output.txt", "r") as f:
    lines = f.readlines()

    for line in lines[1:-1]:
        lst = line.strip().split(":")
        k, v_lst = lst[0], lst[1:]
        dct[k[1:-1]] = ":".join(v_lst) if v_lst != ["NULL"] else ""


def get_idx(dct, lst):
    for i, w in enumerate(lst):
        if w == dct:
            return i
    return None

lst = {
    "general_state": [
        "Удовлетворительное",
        "Средней тяжести",
        "Тяжелое",
        "Терминальное",
    ],
    "consciousness": ["Ясное", "Оглушение", "Сопор", "Кома"],
    "position": ["Активное", "Пассивное", "Вынужденное"],
    "skin": [
        "Сухие",
        "Влажные",
        "Обычной окраски",
        "Бледные",
        "Гиперемия",
        "Цианоз",
        "Желтушность",
    ],
    "dyspnea": ["Эксператорная", "Инспираторная", "Смешанная"],
    "auscultatory": [
        "Везикулярное",
        "Жесткое",
        "Бронхиалоное",
        "Пузрильное",
        "Ослаблено",
        "Отсутствует",
    ],
    "wheezing": ["Свистящие", "Жужжащие"],
    "wet": ["Мелко", "Средне", "Крупнопузырчатые"],
    "percussion_sound": [
        "Легочный",
        "Тимпанический",
        "Коробочный",
        "Притупленный",
        "Тупой",
    ],
    "cough": ["Сухой", "Влажный", "Лающий", "Отсутствует"],
    "rhythmic_arrhythmic": ["Ритмичный", "Аритмичный"],
    "heart_sounds": ["Звучные", "Приглушены", "Глухие"],
    "noise_systolic_diasystolic": ["Систолический", "Диастолический"],
    "tongue": ["Сухой", "Влажный", "Обложен"],
    "painful": ["Безболезненный", "Болезненный"],
    "behavior": ["Спокойное", "Беспокойное", "Возбужден"],
    "speech": ["Внятная", "Дизартрия", "Афазия"],
    "pupils": ["Обычные", "Широкие", "Узкие"],
}

idx = 0
doc = MDoc()
doc.create()
doc.dynamic_pole("ЖАЛОБЫ", "", dct["complaints"])
doc.dynamic_pole(
    "АНАМНЕЗ", "(в т.ч.- эпид.,аллерг.,гинекол. по показаниям)", dct["anamnesis"]
)
doc.text("ОБЪЕКТИВНО:", "")
doc.underline(
    "Общее состояние (",
    ["удовл.", "ср.тяжести", "тяжелое", "терминальное"],
    get_idx(dct["general_state"], lst["general_state"]),
)
doc.underline(
    "). Сознание:",
    lst["consciousness"],
    get_idx(dct["consciousness"], lst["consciousness"]),
)
doc.pdf.write(2, ".")
doc.ln()
doc.underline("Положение ", lst["position"], get_idx(dct["position"], lst["position"]))
doc.input(dct["position_text"])
doc.ln()
doc.underline("Кожные покровы:", lst["skin"], get_idx(dct["skin"], lst["skin"]))
doc.input(dct["skin_text"])
doc.ln()
doc.multipole(["Сыпь", "Зев", "Миндалины"], [dct["rash"], dct["zev"], dct["tonsils"]])
doc.ln()
doc.multipole(
    ["Лимфоузлы", "Пролежни", "Отеки", "t°C"],
    [dct["lymph_nodes"], dct["bedsores"], dct["edema"], dct["temperature"]],
)
doc.ln()
doc.gap("Органы дыхания: ЧДД", dct["respiratory_rate"])
doc.underline("в мин., одышка", lst["dyspnea"], get_idx(dct["dyspnea"], lst["dyspnea"]))
doc.static_pole("", ". Патологическое дыхание", dct["pathological_breathing"])
doc.ln()
doc.underline(
    "Аускультативно: ",
    lst["auscultatory"],
    get_idx(dct["auscultatory"], lst["auscultatory"]),
)
doc.static_pole("", "в", dct["auscultatory_text"])
doc.ln()
doc.underline(
    "Хрипы сухие (", lst["wheezing"], get_idx(dct["wheezing"], lst["wheezing"])
)
doc.static_pole("", ") в", dct["wheezing_text"])
doc.ln()
doc.underline(
    "Влажные (",
    ["мелко-", "средне-", "крупнопузырчатые"],
    get_idx(dct["wet"], lst["wet"]),
)
doc.static_pole("", ") в", dct["wet_text"])
doc.ln()
doc.static_pole("", "Крепитация, шум трения плевры над", dct["crepitus"])
doc.ln()
doc.underline(
    "Перкуторный звук",
    lst["percussion_sound"],
    get_idx(dct["percussion_sound"], lst["percussion_sound"]),
)
doc.static_pole("", "над", dct["percussion_sound_text"])
doc.ln()
doc.underline("Кашель", lst["cough"], get_idx(dct["cough"], lst["cough"]))
doc.static_pole("", ". Мокрота", dct["sputum"])
doc.ln()
doc.text("Органы кровообращения:", "")
doc.gap("пульс", dct["pulse"])
doc.underline(
    "в мин.,",
    lst["rhythmic_arrhythmic"],
    get_idx(dct["rhythmic_arrhythmic"], lst["rhythmic_arrhythmic"]),
)
doc.gap("наполнение", dct["filling"])
doc.gap("ЧСС", dct["heart_rate"])
doc.text("", "в мин.")
doc.ln()
doc.gap("дефицит пульса", dct["pulse_deficit"])
doc.gap("АД", dct["arterial_pressure"])
doc.gap("привычное", dct["habitual"])
doc.gap("максимальное", dct["maximum"])
doc.text("", "мм.рт.ст.")
doc.ln()
doc.underline(
    "Тоны сердца",
    lst["heart_sounds"],
    get_idx(dct["heart_sounds"], lst["heart_sounds"]),
)
doc.underline(
    ". Шум",
    lst["noise_systolic_diasystolic"],
    get_idx(dct["noise_systolic_diasystolic"], lst["noise_systolic_diasystolic"]),
)
doc.static_pole("", "на", dct["noise_on"])
doc.ln()
doc.multipole(
    ["проводится", "Шум трения перикарда. Акцент тона", "на"],
    [dct["held"], dct["accent"], dct["tone"]],
)
doc.ln()
doc.text("Органы пищеварения:", "")
doc.underline("Язык", lst["tongue"], get_idx(dct["tongue"], lst["tongue"]))
doc.static_pole("", "", dct["tongue_text"])
doc.ln()
doc.gap("Живот форма", dct["belly_shape"])
doc.static_pole("", "", dct["tense"])
doc.ln()
doc.underline("", lst["painful"], get_idx(dct["painful"], lst["painful"]))
doc.gap("", dct["painful_text"])
doc.pdf.line(
    doc.pdf.get_x() + 1,
    doc.pdf.get_y() + 2,
    doc.page_limit - 64 + doc.left,
    doc.pdf.get_y() + 2,
)
doc.pdf.set_x(doc.page_limit - 65 + doc.left)
doc.pdf.write(2, "Положительные симптомы (Образцова,")
doc.ln()
doc.static_pole(
    "",
    "Ровзинга, Ситковского, Ортнера, Мерфи, Мейро-Робонса, Щеткина-Блюмберга, Вааля)",
    dct["positive_symptoms"],
)
doc.ln()
doc.multipole(
    ["Перистальтика", "Печень", "Селезенка"],
    [dct["peristalsis"], dct["liver"], dct["spleen"]],
)
doc.ln()
doc.multipole(
    ["Рвота (частота)", "Стул (консистенция, частота)"], [dct["vomit"], dct["feces"]]
)
doc.ln()
doc.text("Нервная система:", "")
doc.underline("Поведение", lst["behavior"], get_idx(dct["behavior"], lst["behavior"]))
doc.static_pole("", ". Контакт", dct["contact"])
doc.ln()
doc.gap("Чувствительность", dct["sensitivity"])
doc.underline("Речь (", lst["speech"], get_idx(dct["speech"], lst["speech"]))
doc.static_pole("", ")", dct["speech_text"])
doc.ln()
doc.underline("Зрачки", lst["pupils"], get_idx(dct["pupils"], lst["pupils"]))
doc.multipole([". Фотореакция", "Нистагм"], [dct["photoreaction"], dct["nystagmus"]])
doc.ln()
doc.gap("Ассиметрия лица", dct["facial_asymmetry"])
doc.pdf.line(
    doc.pdf.get_x() + 1,
    doc.pdf.get_y() + 2,
    doc.page_limit - 87 + doc.left,
    doc.pdf.get_y() + 2,
)
doc.pdf.set_x(doc.page_limit - 88 + doc.left)
doc.pdf.write(2, "Менингеальные симптомы (ригидность затылочных мышц,")
doc.ln()
doc.multipole(
    ["Кенинга, Брудзинского)", "Очаговые симптомы"],
    [dct["meningeal_symptoms_text"], dct["focal_symptoms"]],
)
doc.ln()
doc.static_pole("", "Координатные пробы", dct["coordinator_samples"])
doc.ln()
doc.static_pole("", "Мочеполовая система", dct["genitourinary_system"])
doc.ln()
doc.static_pole("", "Симптом поколачивания", dct["tapping_symptom"])
doc.ln()
doc.dynamic_pole("", "Status locales", dct["status_localis"])
doc.dynamic_pole(
    "Данные инструментальных исследований (ЭКГ, глюкометрия, пульсоксиметрия и пр.)",
    "",
    dct["instrumental_research"],
)
doc.dynamic_pole(
    "Оказанная помощь и ее эффект (в т.ч. результаты инстр. иссл. в динамике)",
    "",
    dct["assistance"],
)
doc.static_pole("Рекомендации:", "", dct["recommendations"])
doc.ln()
doc.static_pole("Сигнальная карта:", "", dct["signal_card"])
doc.ln()
doc.text("Расходные материалы: Салфетки спиртовые №", "")
doc.gap("", dct["alcohol_wipes"])
doc.text(",Бахилы", "")
doc.gap("", dct["shoe_covers"])
doc.text(",Перчатки", "")
doc.gap("", dct["gloves"])
doc.text(",Маска", "")
doc.gap("", dct["mask"])
doc.text(",Шпатель", "")
doc.gap("", dct["hat"])
doc.text("", ",")
doc.ln()
doc.text("Чехол д.терм", "")
doc.gap("", dct["case"])
doc.text(",Шприц 2,0 №", "")
doc.gap("", dct["syringe2"])
doc.text("5,0 №", "")
doc.gap("", dct["syringe5"])
doc.text("10,0 №", "")
doc.gap("", dct["syringe10"])
doc.text("20,0 №", "")
doc.gap("", dct["syringe20"])
doc.text(",Катерер. куб.", "")
doc.gap("", dct["catheter"])
doc.text("G Фикс. пластырь", "")
doc.gap("", dct["patch"])
doc.text("", ",")
doc.ln()
doc.text("Скариф", "")
doc.gap("", dct["scarif"])
doc.text("Тест полоски", "")
doc.gap("", dct["test_strip"])
doc.text(",Пакет мед.отхлд.", "")
doc.gap("", dct["package"])
doc.text(",Маска для небулайзера", "")
doc.gap("", dct["nebulizer_mask"])
doc.ln()
doc.static_pole("", "", "")
doc.ln()
doc.multipole(
    ["Дата и номер наряда", "Подпись", "Карту проверил"],
    [dct["date"], dct["order_number"], dct["checked"]],
)

doc.generate()
