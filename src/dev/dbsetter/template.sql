CREATE TABLE IF NOT EXISTS "template" (
  "id" SERIAL PRIMARY KEY,
  "user_id" INTEGER NOT NULL,
  "template_name" VARCHAR(50) NOT NULL,
  "complaints" TEXT,
  "anamnesis" TEXT,
  "general_state" VARCHAR(20),
  "consciousness" VARCHAR(15),
  "position" VARCHAR(15),
  "position_text" TEXT,
  "skin" VARCHAR(20),
  "skin_text" TEXT,
  "rash" TEXT,
  "zev" TEXT,
  "tonsils" TEXT,
  "lymph_nodes" TEXT,
  "bedsores" TEXT,
  "edema" TEXT,
  "temperature" REAL,
  "respiratory_rate" INTEGER,
  "dyspnea" VARCHAR(20),
  "pathological_breathing" TEXT,
  "auscultatory" VARCHAR(100) NOT NULL,
  "auscultatory_text" TEXT,
  "wheezing" VARCHAR(25),
  "wheezing_text" TEXT,
  "wet" VARCHAR(50),
  "wet_text" TEXT,
  "crepitus" TEXT,
  "percussion_sound" VARCHAR(50),
  "percussion_sound_text" TEXT,
  "cough" VARCHAR(15),
  "sputum" TEXT,
  "pulse" INTEGER,
  "rhythmic_arrhythmic" VARCHAR(15),
  "filling" TEXT,
  "heart_rate" INTEGER,
  "pulse_deficit" TEXT,
  "arterial_pressure" TEXT,
  "habitual" TEXT,
  "maximum" TEXT,
  "heart_sounds" VARCHAR(20),
  "noise_systolic_diasystolic" VARCHAR(20),
  "noise_on" TEXT,
  "held" TEXT,
  "accent" TEXT,
  "tone" TEXT,
  "tongue" VARCHAR(20),
  "tongue_text" TEXT,
  "belly_shape" VARCHAR(50),
  "tense" TEXT,
  "painful" VARCHAR(20),
  "painful_text" TEXT,
  "positive_symptoms" TEXT,
  "peristalsis" TEXT,
  "liver" TEXT,
  "spleen" TEXT,
  "vomit" TEXT,
  "feces" TEXT,
  "behavior" VARCHAR(20),
  "contact" TEXT,
  "sensitivity" TEXT,
  "speech" VARCHAR(10),
  "speech_text" TEXT,
  "pupils" VARCHAR(10),
  "photoreaction" TEXT,
  "nystagmus" TEXT,
  "facial_asymmetry" TEXT,
  "meningeal_symptoms" VARCHAR(50),
  "meningeal_symptoms_text" VARCHAR(50),
  "focal_symptoms" TEXT,
  "coordinator_samples" TEXT,
  "genitourinary_system" TEXT,
  "tapping_symptom" TEXT,
  "status_localis" TEXT,
  "instrumental_research" TEXT,
  "assistance" TEXT,
  "recommendations" TEXT,
  "signal_card" TEXT,
  "alcohol_wipes" INTEGER,
  "shoe_covers" INTEGER,
  "gloves" INTEGER,
  "mask" INTEGER,
  "hat" INTEGER,
  "case" INTEGER,
  "syringe2" INTEGER,
  "syringe5" INTEGER,
  "syringe10" INTEGER,
  "syringe20" INTEGER,
  "catheter" INTEGER,
  "patch" INTEGER,
  "scarif" INTEGER,
  "test_strip" INTEGER,
  "package" INTEGER,
  "nebulizer_mask" INTEGER,
  "date" TEXT, 
  "order_number" TEXT,
  "checked" VARCHAR(100)
);

COMMENT ON TABLE public."template" IS 'Шаблон';
COMMENT ON COLUMN public."template".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."template".user_id IS 'ID пользователя(врача)';
COMMENT ON COLUMN public."template".template_name IS 'Название шаблона';
COMMENT ON COLUMN public."template".complaints IS 'Жалобы';
COMMENT ON COLUMN public."template".anamnesis IS 'Анамнез';
COMMENT ON COLUMN public."template".general_state IS 'Общее состояние';
COMMENT ON COLUMN public."template".consciousness IS 'Сознание';
COMMENT ON COLUMN public."template".position IS 'Положение (активное, пассивное, вынужденное)';
COMMENT ON COLUMN public."template".position_text IS 'Положение текст';
COMMENT ON COLUMN public."template".skin IS 'Кожные покровы';
COMMENT ON COLUMN public."template".skin_text IS 'Кожные покровы текст';
COMMENT ON COLUMN public."template".rash IS 'Сыпь';
COMMENT ON COLUMN public."template".zev IS 'Зев';
COMMENT ON COLUMN public."template".tonsils IS 'Миндалины';
COMMENT ON COLUMN public."template".lymph_nodes IS 'Лимфоузлы';
COMMENT ON COLUMN public."template".bedsores IS 'Пролежни';
COMMENT ON COLUMN public."template".edema IS 'Отеки';
COMMENT ON COLUMN public."template".temperature IS 'Темепратура';
COMMENT ON COLUMN public."template".respiratory_rate IS 'ЧДД - частота дыхательных движений';
COMMENT ON COLUMN public."template".dyspnea IS 'Одышка';
COMMENT ON COLUMN public."template".pathological_breathing IS 'Патологическое дыхание';
COMMENT ON COLUMN public."template".auscultatory IS 'Аускультативно';
COMMENT ON COLUMN public."template".auscultatory_text IS 'Аускультативно текст';
COMMENT ON COLUMN public."template".wheezing IS 'Хрипы';
COMMENT ON COLUMN public."template".wheezing_text IS 'Хрипы текст';
COMMENT ON COLUMN public."template".wet IS 'Влажные';
COMMENT ON COLUMN public."template".wet_text IS 'Влажные текст';
COMMENT ON COLUMN public."template".crepitus IS 'Крепитация, шум трения плевры над';
COMMENT ON COLUMN public."template".percussion_sound IS 'Перкуторный звук';
COMMENT ON COLUMN public."template".percussion_sound_text IS 'Перкуторный звук текст';
COMMENT ON COLUMN public."template".cough IS 'Кашель';
COMMENT ON COLUMN public."template".sputum IS 'Мокрота';
COMMENT ON COLUMN public."template".pulse IS 'Пульс';
COMMENT ON COLUMN public."template".rhythmic_arrhythmic IS 'Ритмичный/аритмичный';
COMMENT ON COLUMN public."template".filling IS 'Наполнение';
COMMENT ON COLUMN public."template".heart_rate IS 'ЧСС - частота сердечных сокращений';
COMMENT ON COLUMN public."template".pulse_deficit IS 'Дефицит пульса';
COMMENT ON COLUMN public."template".arterial_pressure IS 'АД - артериальное давление';
COMMENT ON COLUMN public."template".habitual IS 'Привычное';
COMMENT ON COLUMN public."template".maximum IS 'Максимальное';
COMMENT ON COLUMN public."template".heart_sounds IS 'Тоны сердца';
COMMENT ON COLUMN public."template".noise_systolic_diasystolic IS 'Шум систолический/диасистолический';
COMMENT ON COLUMN public."template".noise_on IS 'Шум на';
COMMENT ON COLUMN public."template".held IS 'Проводится';
COMMENT ON COLUMN public."template".accent IS 'Акцент';
COMMENT ON COLUMN public."template".tone IS 'Тона на';
COMMENT ON COLUMN public."template".tongue IS 'Язык';
COMMENT ON COLUMN public."template".tongue_text IS 'Язык текст';
COMMENT ON COLUMN public."template".belly_shape IS 'Форма живота';
COMMENT ON COLUMN public."template".tense IS 'Напряжен в';
COMMENT ON COLUMN public."template".painful IS 'Безболезненный/болезненный';
COMMENT ON COLUMN public."template".painful_text IS 'Безболезненный/болезненный текст';
COMMENT ON COLUMN public."template".positive_symptoms IS 'Положительные симптомы';
COMMENT ON COLUMN public."template".peristalsis IS 'Перистальтика';
COMMENT ON COLUMN public."template".liver IS 'Печень';
COMMENT ON COLUMN public."template".spleen IS 'Селезенка';
COMMENT ON COLUMN public."template".vomit IS 'Рвота';
COMMENT ON COLUMN public."template".feces IS 'Стул';
COMMENT ON COLUMN public."template".behavior IS 'Поведение';
COMMENT ON COLUMN public."template".contact IS 'Контакт';
COMMENT ON COLUMN public."template".sensitivity IS 'Чувствительность';
COMMENT ON COLUMN public."template".speech IS 'Речь';
COMMENT ON COLUMN public."template".speech_text IS 'Речь текст';
COMMENT ON COLUMN public."template".pupils IS 'Зрачки';
COMMENT ON COLUMN public."template".photoreaction IS 'Фотореакция';
COMMENT ON COLUMN public."template".nystagmus IS 'Нистагм';
COMMENT ON COLUMN public."template".facial_asymmetry IS 'Асимметрия лица';
COMMENT ON COLUMN public."template".meningeal_symptoms IS 'Меннингеальные симптомы';
COMMENT ON COLUMN public."template".meningeal_symptoms_text IS 'Меннингеальные симптомы текст';
COMMENT ON COLUMN public."template".focal_symptoms IS 'Очаговые симптомы';
COMMENT ON COLUMN public."template".coordinator_samples IS 'Координаторные пробы';
COMMENT ON COLUMN public."template".genitourinary_system IS 'Мочеполовая система';
COMMENT ON COLUMN public."template".tapping_symptom IS 'Симптом поколачивания';
COMMENT ON COLUMN public."template".status_localis IS 'Статус локалис';
COMMENT ON COLUMN public."template".instrumental_research IS 'Данные инструментальных исследований';
COMMENT ON COLUMN public."template".assistance IS 'Оказание помощи и ее эффект';
COMMENT ON COLUMN public."template".recommendations IS 'Рекомендации';
COMMENT ON COLUMN public."template".signal_card IS 'Сигнальная карта';
COMMENT ON COLUMN public."template".alcohol_wipes IS 'Салфетки спиртовые';
COMMENT ON COLUMN public."template".shoe_covers IS 'Бахилы';
COMMENT ON COLUMN public."template".gloves IS 'Перчатки';
COMMENT ON COLUMN public."template".mask IS 'Маска';
COMMENT ON COLUMN public."template".hat IS 'Шпатель';
COMMENT ON COLUMN public."template".case IS 'Чехол';
COMMENT ON COLUMN public."template".syringe2 IS 'Шприц 2.0';
COMMENT ON COLUMN public."template".syringe5 IS 'Шприц 5.0';
COMMENT ON COLUMN public."template".syringe10 IS 'Шприц 10.0';
COMMENT ON COLUMN public."template".syringe20 IS 'Шприц 20.0';
COMMENT ON COLUMN public."template".catheter IS 'Катетер';
COMMENT ON COLUMN public."template".patch IS 'Пластырь';
COMMENT ON COLUMN public."template".test_strip IS 'Тест полоски';
COMMENT ON COLUMN public."template".package IS 'Пакет медицинский охлажденный';
COMMENT ON COLUMN public."template".nebulizer_mask IS 'Маска для небулайзера';
COMMENT ON COLUMN public."template".date IS 'Дата';
COMMENT ON COLUMN public."template".order_number IS 'Номер наряда';
COMMENT ON COLUMN public."template".checked IS 'Карту проверил';

INSERT INTO "template" ("user_id", "template_name", "complaints", "anamnesis", "general_state", "consciousness", "position", "position_text", "skin", "skin_text", "rash", "zev", "tonsils", "lymph_nodes", "bedsores", "edema", "temperature", "respiratory_rate", "dyspnea", "pathological_breathing", "auscultatory", "auscultatory_text", "wheezing", "wheezing_text", "wet", "wet_text", "crepitus", "percussion_sound", "percussion_sound_text", "cough", "sputum", "pulse", "rhythmic_arrhythmic", "filling", "heart_rate", "pulse_deficit", "arterial_pressure", "habitual", "maximum", "heart_sounds", "noise_systolic_diasystolic", "noise_on", "held", "accent", "tone", "tongue", "tongue_text", "belly_shape", "tense", "painful", "painful_text", "positive_symptoms", "peristalsis", "liver", "spleen", "vomit", "feces", "behavior", "contact", "sensitivity", "speech", "speech_text", "pupils", "photoreaction", "nystagmus", "facial_asymmetry", "meningeal_symptoms", "meningeal_symptoms_text", "focal_symptoms", "coordinator_samples", "genitourinary_system", "tapping_symptom", "status_localis", "instrumental_research", "assistance", "recommendations", "signal_card", "alcohol_wipes", "shoe_covers", "gloves", "mask", "hat", "case", "syringe2", "syringe5", "syringe10", "syringe20", "catheter", "patch", "scarif", "test_strip", "package", "nebulizer_mask", "date", "order_number", "checked") VALUES
  ('1', 'Шаблон1', 'На момент осмотра беспокоит боль в грудной клетке, в межлопаточной области больше слева, усиливается при движении, поворотах туловища, также дискомфорт в левом плечевом суставе.', 'Вышеперечисленные жалобы беспокоят с 04:00 13.08.2022г., однако боли в грудном отделе позвоночника беспокоят периодически, последнее ухудшение около недели связывает с остеохондрозом, по поводу которого неднократно лечился у невролога, а также неоднократно вызывал бригады СМП, ОНМП. Данный вызов повторный. В анамнезе: со слов страдает гипертонической болезнью 1 степени, остеохондрозом, дегенеративными изменениями в позвоночнике. Травмы, операции отрицает. Контакт с COVID 19 и другими крантинными инфекциями отрицает, за пределы Москвы не выезжает, сезонная вакцинация не проводилась. Аллергию отрицает. ЕМИАС, МГФОМС - не информативен.', 'Средней тяжести', 'Ясное', 'Активное', NULL, 'Бледные', 'обычныой влажности', 'Нет', 'Чистый', 'Не увеличены', 'Не увеличены', 'Нет', 'Нет', '36.6', '18', NULL, 'Нет', 'Везикулярное', 'по всем полям', NULL, 'Нет', NULL, 'Нет', 'Нет', 'Легочный', 'по всем полям', 'Отсутствует', 'Нет', '58', 'Ритмичный', 'Удовлетворительное', '58', '0', '130/80', '120/80', '150/90', 'Звучные', NULL, 'Нет', 'Нет', 'II', 'Аорте', 'Влажный', 'чистый, расположен по средней линии', 'Правильная', 'Не напряжен доступен глубокой пальпации', 'Безболезненный', 'во всех отделах', 'Отрицательные', 'Выслушивается', 'Не увеличена', 'Не пальпируется', 'Нет', 'Регулярный - 1 раз в день, оформлен, коричневый', 'Спокойное', 'Контактен', 'Сохранена, D = S', 'Внятная', NULL, 'Обычные', 'Живая', 'Нет', 'Нет', NULL, 'Нет', 'Нет', 'Не выполнялась по тяжести состояния', 'Дизурических расстройств не выявлено, моча желтого цвета', 'Отрицательный с обеих сторон', 'Вес = 97 кг, Рост = 173 см, ИМТ = 32', 'SpO2 99%; ЭКГ(13.08.2022г. 05:28) синусовая брадикардия с ЧСС 58 в мин., ЭОС отклонена влево, ST - изолиния, неспецифические нарушения внутрижелудочкового приведения. ЭКГ для анализа динамики не предоставлено.', 'Расспрос, изучение мед. документов и еще куча всего.', NULL, 'Не требуется', '10', '1', '1', '1', '1', '1', '0', '2', '0', '0', '1', '1', '0', '1', '0', '13.08.2022', '208788714', 'Васильев Д.С.');