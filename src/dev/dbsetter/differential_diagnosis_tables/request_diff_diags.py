# 1 - Акушерство
OBSTETRICS_SQL = \
'''
  SELECT DISTINCT id, term AS "Срок", wdm AS "ВДМ", oj AS "ОЖ"
  FROM obstetrics
  ORDER BY obstetrics.id ASC;
'''

# 2 - Нормы ЧД, ЧСС, АД у детей (в покое)
NORMS_IN_CHILDREN_SQL = \
'''
  SELECT DISTINCT id, age AS "Возраст", weight AS "Вес в кг", respiratory_rate AS "ЧД", heart_rate AS "ЧСС", arterial_pressure AS "АД"
  FROM norms_in_children
  ORDER BY norms_in_children.id ASC;
'''

# 3 - Параметры проведения базовой СЛР
PARAMETRS_CLR_SQL = \
'''
  SELECT DISTINCT id, stage AS "Этап", adults_and_children AS "Взрослые и дети старше 14 лет", children AS "Дети", newborns AS "Новорожденные при рождении"
  FROM parameters_clr
  ORDER BY parameters_clr.id ASC;
'''

# 4 - Промывание желудка у детей
GASTRIC_LAVAGE_IN_CHILDREN_SQL = \
'''
  SELECT DISTINCT id, age AS "Возраст", one_time_volume AS "Разовый объем, мл", maximum_flushing_volume AS "Максимальный объём промывания, мл"
  FROM gastric_lavage_in_children
  ORDER BY gastric_lavage_in_children.id ASC;
'''

# 5 - Размеры эндотрахеальных трубок у детей
SIZE_OF_ENDOTRACHEAL_TUBES_IN_CHILDREN_SQL = \
'''
  SELECT DISTINCT id, age AS "Возраст", weight AS "Вес в кг", inner_diameter AS "Внутренний диаметр, в мм", insertion_depth AS "Глубина введения, в см", suction_catheter AS "Катетер для аспирации FG"
  FROM size_of_endotracheal_tubes_in_children
  ORDER BY size_of_endotracheal_tubes_in_children.id ASC;
'''

# 6 - Соответствие размеров ларннгеальных трубок параметрам пациента
SIZE_OF_LARYNGEAL_TUBE_SQL = \
'''
  SELECT DISTINCT id, patient_parameters AS "Параметры пациента", tube_size AS "Размер трубки", tube_connector_color AS "Цвет коннектора трубки"
  FROM size_of_laryngeal_tube
  ORDER BY size_of_laryngeal_tube.id ASC;
'''

# 7 - ВАШ. НОШ. Шкалы оценки интенсивности боли
PAIN_INTENSITY_SQL = \
'''
  SELECT DISTINCT id, pain_syndrome AS "Интенсивность болевого синдрома", vash_nosh AS "ВАШ НОШ", symptoms AS "Проявление боли, симптомы", therapy AS "Терапия догоспитального этапа"
  FROM pain_intensity
  ORDER BY pain_intensity.id ASC;
'''

# 8 - Острая дыхательная недостаточность (Кассиль В.Л. 2004 г.)
ACUTE_RESPIRATORY_FAILURE_SQL = \
'''
  SELECT DISTINCT id, state AS "Состояние", consciousness AS "Сознание", skin AS "Кожные покровы", arterial_pressure AS "АД", heart_rate AS "ЧСС", respiratory_rate AS "ЧД", spo2 AS "SpO2 при O2 терапии"
  FROM acute_respiratory_failure
  ORDER BY acute_respiratory_failure.id ASC;
'''

# 9 - Оценка мышечной силы по баллам
MUSCLE_STRENGTH_ASSESSMENT_SQL = \
'''
  SELECT DISTINCT id, point AS "Балл", note AS "Описание"
  FROM muscle_strength_assessment
  ORDER BY muscle_strength_assessment.id ASC;
'''

# 10 - Шкала возбуждения-седации Ричмонда (шкала RASS)
RICHMOND_AROUSALSWDATION_SCALE_SQL = \
'''
  SELECT DISTINCT id, points AS "Баллы", term AS "Термин", description AS "Описание"
  FROM richmond_arousal_sedation_scale
  ORDER BY richmond_arousal_sedation_scale.id ASC;
'''

# 11 - Определение площади ожогов у детей (по Lund и Browder)
AREA_BURNS_CHILDREN_SQL = \
'''
  SELECT DISTINCT id, area_affected AS "Область поражения", zero_years AS "0 лет", one_year AS "1 год", five_years AS "5 лет", ten_years AS "10 лет", fifteen_years AS "15 лет"
  FROM area_burns_children
  ORDER BY area_burns_children.id ASC;
'''

# 12 - Шкала оценки вероятности ТЭЛА (Revised Geneva Score)
PROBABILITY_SCALE_SQL = \
'''
  SELECT DISTINCT id, sign AS "Признак", points AS "Баллы"
  FROM probability_scale
  ORDER BY probability_scale.id ASC;
'''

# 13 - Шкала оценки вероятности ТЭЛА (Revised Geneva Score)
PROBABILITY_SCALE_INTERPRETATION_SQL = \
'''
  SELECT DISTINCT id, probability AS "Клиническая вероятность", sum AS "Сумма баллов"
  FROM probability_scale_interpretation
  ORDER BY probability_scale_interpretation.id ASC;
'''

# 14 - Критерии оценки новорождённого по шкале Апгар
NEWBORN_APGAR_CRITERIA_HEART_RATE_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM newborn_apgar_criteria_heart_rate
  ORDER BY newborn_apgar_criteria_heart_rate.id ASC;
'''

# 15 - Критерии оценки новорождённого по шкале Апгар
NEWBORN_APGAR_CRITERIA_BREATH_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM newborn_apgar_criteria_breath
  ORDER BY newborn_apgar_criteria_breath.id ASC;
'''

# 16 - Критерии оценки новорождённого по шкале Апгар
NEWBORN_APGAR_CRITERIA_MUSCLE_TONE_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM newborn_apgar_criteria_muscle_tone
  ORDER BY newborn_apgar_criteria_muscle_tone.id ASC;
'''

# 17 - Критерии оценки новорождённого по шкале Апгар
NEWBORN_APGAR_CRITERIA_REACTION_TO_IRRITATION_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM newborn_apgar_criteria_reaction_to_irritation
  ORDER BY newborn_apgar_criteria_reaction_to_irritation.id ASC;
'''

# 18 - Критерии оценки новорождённого по шкале Апгар
NEWBORN_APGAR_CRITERIA_COLOR_SKIN_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM newborn_apgar_criteria_color_skin
  ORDER BY newborn_apgar_criteria_color_skin.id ASC;
'''

# 19 - Проктокол оценки тяжести состояния пациента (NEWS)
CONDITION_ASSESSMENT_PROTOCOL_BREATHING_RATE_SQL = \
'''
  SELECT DISTINCT id, parameter AS "Параметр", points AS "Расшифровка баллов"
  FROM condition_assessment_protocol_breathing_rate
  ORDER BY condition_assessment_protocol_breathing_rate.id ASC;
'''

# 20 - Проктокол оценки тяжести состояния пациента (NEWS)
CONDITION_ASSESSMENT_PROTOCOL_BLOOD_OXYGEN_SATURATION_SQL = \
'''
  SELECT DISTINCT id, parameter AS "Параметр", points AS "Расшифровка баллов"
  FROM condition_assessment_protocol_blood_oxygen_saturation
  ORDER BY condition_assessment_protocol_blood_oxygen_saturation.id ASC;
'''

# 21 - Проктокол оценки тяжести состояния пациента (NEWS)
CONDITION_ASSESSMENT_PROTOCOL_OXYGEN_INSUFFLATION_SQL = \
'''
  SELECT DISTINCT id, parameter AS "Параметр", points AS "Расшифровка баллов"
  FROM condition_assessment_protocol_oxygen_insufflation
  ORDER BY condition_assessment_protocol_oxygen_insufflation.id ASC;
'''

# 22 - Проктокол оценки тяжести состояния пациента (NEWS)
CONDITION_ASSESSMENT_PROTOCOL_BODY_TEMPERATURE_SQL = \
'''
  SELECT DISTINCT id, parameter AS "Параметр", points AS "Расшифровка баллов"
  FROM condition_assessment_protocol_body_temperature
  ORDER BY condition_assessment_protocol_body_temperature.id ASC;
'''

# 23 - Проктокол оценки тяжести состояния пациента (NEWS)
CONDITION_ASSESSMENT_PROTOCOL_SYSTOLIC_BLOOD_PRESSURE_SQL = \
'''
  SELECT DISTINCT id, parameter AS "Параметр", points AS "Расшифровка баллов"
  FROM condition_assessment_protocol_systolic_blood_pressure
  ORDER BY condition_assessment_protocol_systolic_blood_pressure.id ASC;
'''

# 24 - Проктокол оценки тяжести состояния пациента (NEWS)
CONDITION_ASSESSMENT_PROTOCOL_HEART_RATE_SQL = \
'''
  SELECT DISTINCT id, parameter AS "Параметр", points AS "Расшифровка баллов"
  FROM condition_assessment_protocol_heart_rate
  ORDER BY condition_assessment_protocol_heart_rate.id ASC;
'''

# 25 - Проктокол оценки тяжести состояния пациента (NEWS)
CONDITION_ASSESSMENT_PROTOCOL_LEVEL_CONSCIOUSNESS_SQL = \
'''
  SELECT DISTINCT id, parameter AS "Параметр", points AS "Расшифровка баллов"
  FROM condition_assessment_protocol_level_of_consciousness
  ORDER BY condition_assessment_protocol_level_of_consciousness.id ASC;
'''

# 26 - Проктокол оценки тяжести состояния пациента (NEWS)
CONDITION_ASSESSMENT_PROTOCOL_COVID_SQL = \
'''
  SELECT DISTINCT id, parameter AS "Параметр", points AS "Расшифровка баллов"
  FROM condition_assessment_protocol_covid;
  ORDER BY condition_assessment_protocol_covid.id ASC;
'''

# 27 - Проктокол оценки тяжести состояния пациента (NEWS)
CONDITION_ASSESSMENT_PROTOCOL_INTERPRETATION_SQL = \
'''
  SELECT DISTINCT id, point AS "Балл", action AS "Действие"
  FROM condition_assessment_protocol_interpretation
  ORDER BY condition_assessment_protocol_interpretation.id ASC;
'''

# 28 - ХСН ШОКС (в модификации Мареева В.Ю.)
STATUS_RATING_SCALE_DYSPNEA_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM status_rating_scale_dyspnea
  ORDER BY status_rating_scale_dyspnea.id ASC;
'''

# 29 - ХСН ШОКС (в модификации Мареева В.Ю.)
STATUS_RATING_SCALE_WEIGHT_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM status_rating_scale_weight
  ORDER BY status_rating_scale_weight.id ASC;
'''

# 30 - ХСН ШОКС (в модификации Мареева В.Ю.)
STATUS_RATING_SCALE_HEART_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM status_rating_scale_heart
  ORDER BY status_rating_scale_heart.id ASC;
'''

# 31 - ХСН ШОКС (в модификации Мареева В.Ю.)
STATUS_RATING_SCALE_POSITION_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM status_rating_scale_position
  ORDER BY status_rating_scale_position.id ASC;
'''

# 32 - ХСН ШОКС (в модификации Мареева В.Ю.)
STATUS_RATING_SCALE_NECK_VEINS_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM status_rating_scale_neck_veins
  ORDER BY status_rating_scale_neck_veins.id ASC;
'''

# 33 - ХСН ШОКС (в модификации Мареева В.Ю.)
STATUS_RATING_SCALE_WHEEZING_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM status_rating_scale_wheezing
  ORDER BY status_rating_scale_wheezing.id ASC;
'''

# 34 - ХСН ШОКС (в модификации Мареева В.Ю.)
STATUS_RATING_SCALE_GALLOP_RHYTHM_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM status_rating_scale_gallop_rhythm
  ORDER BY status_rating_scale_gallop_rhythm.id ASC;
'''

# 35 - ХСН ШОКС (в модификации Мареева В.Ю.)
STATUS_RATING_SCALE_LIVER_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM status_rating_scale_liver
  ORDER BY status_rating_scale_liver.id ASC;
'''

# 36 - ХСН ШОКС (в модификации Мареева В.Ю.)
STATUS_RATING_SCALE_EDEMA_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM status_rating_scale_edema
  ORDER BY status_rating_scale_edema.id ASC;
'''

# 37 - ХСН ШОКС (в модификации Мареева В.Ю.)
STATUS_RATING_SCALE_LEVEL_SAD_SQL = \
'''
  SELECT DISTINCT id, description AS "Описание", point AS "Балл"
  FROM status_rating_scale_level_sad
  ORDER BY status_rating_scale_level_sad.id ASC;
'''

# 38 - ХСН ШОКС (в модификации Мареева В.Ю.)
STATUS_RATING_SCALE_INTERPRETATION_SQL = \
'''
  SELECT DISTINCT id, point AS "Балл", sign AS "Признак"
  FROM status_rating_scale_interpretation
  ORDER BY status_rating_scale_interpretation.id ASC;
'''

# 39 - Шкала Глазго (Glasgow Coma Scale)
GLASGOW_COMA_SCALE_ADULTS_SQL = \
'''
  SELECT DISTINCT id, type AS "Действие", action AS "Ответ на действие", point AS "Балл"
  FROM glasgow_coma_scale_adults
  ORDER BY glasgow_coma_scale_adults.id ASC;
'''

# 40 - Шкала Глазго (Glasgow Coma Scale)
GLASGOW_COMA_SCALE_CHILDREN_SQL = \
'''
  SELECT DISTINCT id, type AS "Действие", action AS "Ответ на действие", point AS "Балл"
  FROM glasgow_coma_scale_children
  ORDER BY glasgow_coma_scale_children.id ASC;
'''

# 41 - Шкала Глазго (Glasgow Coma Scale)
GLASGOW_COMA_SCALE_NEWBORNS_SQL = \
'''
  SELECT DISTINCT id, type AS "Действие", action AS "Ответ на действие", point AS "Балл"
  FROM glasgow_coma_scale_newborns
  ORDER BY glasgow_coma_scale_newborns.id ASC;
'''

# 42 - Шкала Глазго (Glasgow Coma Scale)
GLASGOW_COMA_SCALE_INTERPRETATION_SQL = \
'''
  SELECT DISTINCT id, point AS "Балл", sign AS "Признак"
  FROM glasgow_coma_scale_interpretation
  ORDER BY glasgow_coma_scale_interpretation.id ASC;
'''

# 43 - Шкала комы FOUR
COMA_SCALE_EYE_REACTIONS_SQL = \
'''
  SELECT DISTINCT id, sign AS "Признак", points AS "Баллы"
  FROM coma_scale_eye_reactions
  ORDER BY coma_scale_eye_reactions.id ASC;
'''

# 44 - Шкала комы FOUR
COMA_SCALE_MOTOR_REACTIONS_SQL = \
'''
  SELECT DISTINCT id, sign AS "Признак", points AS "Баллы"
  FROM coma_scale_motor_reactions
  ORDER BY coma_scale_motor_reactions.id ASC;
'''

# 45 - Шкала комы FOUR
COMA_SCALE_STEM_REFLEXES_SQL = \
'''
  SELECT DISTINCT id, sign AS "Признак", points AS "Баллы"
  FROM coma_scale_stem_reflexes
  ORDER BY coma_scale_stem_reflexes.id ASC;
'''

# 46 - Шкала комы FOUR
COMA_SCALE_BREATHING_PATTERN_SQL = \
'''
  SELECT DISTINCT id, sign AS "Признак", points AS "Баллы"
  FROM coma_scale_breathing_pattern
  ORDER BY coma_scale_breathing_pattern.id ASC;
'''

# 47 - Шкала комы FOUR
COMA_SCALE_INTERPRETATION_SQL = \
'''
  SELECT DISTINCT id, point AS "Балл", sign AS "Признак"
  FROM coma_scale_interpretation
  ORDER BY coma_scale_interpretation.id ASC;
'''

# 48 - Шкала моторного дефицита LAMS (Los Angeles Motor Scale)
MOTOR_DEFICIT_SCALE_FACIAL_ASYMMETRY_SQL = \
'''
  SELECT DISTINCT id, sign AS "Признак", points AS "Баллы"
  FROM motor_deficit_scale_facial_asymmetry
  ORDER BY motor_deficit_scale_facial_asymmetry.id ASC;
'''

# 49 - Шкала моторного дефицита LAMS (Los Angeles Motor Scale)
MOTOR_DEFICIT_SCALE_HOLDING_HANDS_SQL = \
'''
  SELECT DISTINCT id, sign AS "Признак", points AS "Баллы"
  FROM motor_deficit_scale_holding_hands
  ORDER BY motor_deficit_scale_holding_hands.id ASC;
'''

# 50 - Шкала моторного дефицита LAMS (Los Angeles Motor Scale)
MOTOR_DEFICIT_SCALE_SQUEEZING_BRUSH_SQL = \
'''
  SELECT DISTINCT id, sign AS "Признак", points AS "Баллы"
  FROM motor_deficit_scale_squeezing_brush
  ORDER BY motor_deficit_scale_squeezing_brush.id ASC;
'''

# Словарь
DATA = {
    'Акушерство': {
        'sql': [OBSTETRICS_SQL],
        'subtables_name': [],
        'part_name': '',
        'note': '',
        'type_table': 1,
        'type_result': 1
    },
    'Нормы ЧД, ЧСС, АД у детей (в покое)': {
        'sql': [NORMS_IN_CHILDREN_SQL],
        'subtables_name': [],
        'part_name': '',
        'note': '',
        'type_table': 1,
        'type_result': 1
    },
    'Параметры проведения базовой СЛР': {
        'sql': [PARAMETRS_CLR_SQL],
        'subtables_name': [],
        'part_name': '',
        'note': 'РЕАНИМАЦИОННЫЕ МЕРОПРИЯТИЯ ПРЕКРАЩАЮТСЯ: при неэффективности в течение 30 минут, при отсутствии у новорожденного при рождении сердцебиения по истечении 10 минут с начала проведения СЛР в полном объеме (ИВЛ, массаж сердца, введение препаратов). Реанимационные мероприятия проводятся в течение 30 минут от последнего зарегистрированного эпизода электрической активности сердца!!!',
        'type_table': 1,
        'type_result': 1
    },
    'Промывание желудка у детей': {
        'sql': [GASTRIC_LAVAGE_IN_CHILDREN_SQL],
        'subtables_name': [],
        'part_name': '',
        'note': '',
        'type_table': 1,
        'type_result': 1
    },
    'Размеры эндотрахеальных трубок у детей': {
        'sql': [SIZE_OF_ENDOTRACHEAL_TUBES_IN_CHILDREN_SQL],
        'subtables_name': [],
        'part_name': '',
        'note': 'Глубина стояния трубки 6 см + масса тела ребенка в кг.',
        'type_table': 1,
        'type_result': 1
    },
    'Соответствие размеров ларннгеальных трубок параметрам пациента': {
        'sql': [SIZE_OF_LARYNGEAL_TUBE_SQL],
        'subtables_name': [],
        'part_name': '',
        'note': '',
        'type_table': 1,
        'type_result': 1
    },
    'ВАШ. НОШ. Шкалы оценки интенсивности боли': {
        'sql': [PAIN_INTENSITY_SQL],
        'subtables_name': [],
        'part_name': 'Интенсивность боли',
        'note': '',
        'type_table': 2,
        'type_result': 3
    },
    'Острая дыхательная недостаточность (Кассиль В.Л. 2004 г.)': {
        'sql': [ACUTE_RESPIRATORY_FAILURE_SQL],
        'subtables_name': [],
        'part_name': '',
        'note': '',
        'type_table': 2,
        'type_result': 2
    },
    'Оценка мышечной силы по баллам': {
        'sql': [MUSCLE_STRENGTH_ASSESSMENT_SQL],
        'subtables_name': [],
        'part_name': 'Мышечная сила',
        'note': '',
        'type_table': 2,
        'type_result': 3
    },
    'Шкала возбуждения-седации Ричмонда (шкала RASS)': {
        'sql': [RICHMOND_AROUSALSWDATION_SCALE_SQL],
        'subtables_name': [],
        'part_name': 'Шкала возбуждения-седации Ричмонда',
        'note': '',
        'type_table': 2,
        'type_result': 3
    },
    'Определение площади ожогов у детей (по Lund и Browder)': {
        'sql': [AREA_BURNS_CHILDREN_SQL],
        'subtables_name': [],
        'part_name': 'Площадь ожогов',
        'note': '',
        'type_table': 3,
        'type_result': 4
    },
    'Шкала оценки вероятности ТЭЛА (Revised Geneva Score)': {
        'sql': [PROBABILITY_SCALE_SQL,
                PROBABILITY_SCALE_INTERPRETATION_SQL],
        'subtables_name': ['Шкала оценки вероятности ТЭЛА (Revised Geneva Score)',
                           'Интерпретация результата'],
        'part_name': 'Шкала оценки вероятности ТЭЛА',
        'note': '',
        'type_table': 3,
        'type_result': 5
    },
    'Критерии оценки новорождённого по шкале Апгар': {
        'sql': [NEWBORN_APGAR_CRITERIA_HEART_RATE_SQL,
                NEWBORN_APGAR_CRITERIA_BREATH_SQL,
                NEWBORN_APGAR_CRITERIA_MUSCLE_TONE_SQL,
                NEWBORN_APGAR_CRITERIA_REACTION_TO_IRRITATION_SQL,
                NEWBORN_APGAR_CRITERIA_COLOR_SKIN_SQL],
        'subtables_name': ['ЧСС',
                           'Дыхание',
                           'Мышечный тонус',
                           'Реакция на фарингеальный катетер (на раздражение)',
                           'Цвет кожи'],
        'part_name': '',
        'note': 'Оценка проводится на 1-й и 5-й минуте после рождения, независимо от характера и объема проводимых реанимационных мероприятий. В случае продолжения реанимационных мероприятий более 5 минут жизни, проводится третья оценка по Апгар через 10 минут после рождения. Признаки живорожденности: самостоятельное дыхание, сердцебиение, пульсация пуповины и произвольное движение мышц.',
        'type_table': 4,
        'type_result': 6
    },
    'Проктокол оценки тяжести состояния пациента (NEWS)': {
        'sql': [CONDITION_ASSESSMENT_PROTOCOL_BREATHING_RATE_SQL,
                CONDITION_ASSESSMENT_PROTOCOL_BLOOD_OXYGEN_SATURATION_SQL,
                CONDITION_ASSESSMENT_PROTOCOL_OXYGEN_INSUFFLATION_SQL,
                CONDITION_ASSESSMENT_PROTOCOL_BODY_TEMPERATURE_SQL,
                CONDITION_ASSESSMENT_PROTOCOL_SYSTOLIC_BLOOD_PRESSURE_SQL,
                CONDITION_ASSESSMENT_PROTOCOL_HEART_RATE_SQL,
                CONDITION_ASSESSMENT_PROTOCOL_LEVEL_CONSCIOUSNESS_SQL,
                CONDITION_ASSESSMENT_PROTOCOL_COVID_SQL,
                CONDITION_ASSESSMENT_PROTOCOL_INTERPRETATION_SQL],
        'subtables_name': ['Частота дыхания за 1 минуту',
                           'Насыщение крови кислородом, %',
                           'Необходимость инсуффляции кислорода',
                           'Температура тела',
                           'Систолическое артериальное давление, мм.рт.ст.',
                           'Частота сердечных сокращений в 1 минуту',
                           'Изменение уровня сознания',
                           'Пациент с COVID-19',
                           'Интерпретация результата'],
        'part_name': 'Тяжесть состояния пациента',
        'note': '',
        'type_table': 4,
        'type_result': 5
    },
    'ХСН ШОКС (в модификации Мареева В.Ю.)': {
        'sql': [STATUS_RATING_SCALE_DYSPNEA_SQL,
                STATUS_RATING_SCALE_WEIGHT_SQL,
                STATUS_RATING_SCALE_HEART_SQL,
                STATUS_RATING_SCALE_POSITION_SQL,
                STATUS_RATING_SCALE_NECK_VEINS_SQL,
                STATUS_RATING_SCALE_WHEEZING_SQL,
                STATUS_RATING_SCALE_GALLOP_RHYTHM_SQL,
                STATUS_RATING_SCALE_LIVER_SQL,
                STATUS_RATING_SCALE_EDEMA_SQL,
                STATUS_RATING_SCALE_LEVEL_SAD_SQL,
                STATUS_RATING_SCALE_INTERPRETATION_SQL],
        'subtables_name': ['Одышка',
                           'Изменился ли за последнюю неделю вес',
                           'Жалобы на перебои в работе сердца',
                           'В каком положении находится в постели',
                           'Набухшие шейные вены',
                           'Хрипы в легких',
                           'Наличие ритма галопа',
                           'Печень',
                           'Отеки',
                           'Уровень САД',
                           'Интерпретация результата'],
        'part_name': 'Клиническое состояние больного ХСН (ШОКС)',
        'note': '',
        'type_table': 4,
        'type_result': 6
    },
    'Шкала Глазго (Glasgow Coma Scale)': {
        'sql': [GLASGOW_COMA_SCALE_ADULTS_SQL,
                GLASGOW_COMA_SCALE_CHILDREN_SQL,
                GLASGOW_COMA_SCALE_NEWBORNS_SQL,
                GLASGOW_COMA_SCALE_INTERPRETATION_SQL],
        'subtables_name': ['Взрослые и детей старше 4 лет',
                           'Дети от 1 до 4 лет',
                           'Грудные дети (до 1 года)',
                           'Интерпретация результата'],
        'part_name': 'Шкала Глазго',
        'note': '',
        'type_table': 4,
        'type_result': 7
    },
    'Шкала комы FOUR': {
        'sql': [COMA_SCALE_EYE_REACTIONS_SQL,
                COMA_SCALE_MOTOR_REACTIONS_SQL,
                COMA_SCALE_STEM_REFLEXES_SQL,
                COMA_SCALE_BREATHING_PATTERN_SQL,
                COMA_SCALE_INTERPRETATION_SQL],
        'subtables_name': ['Глазные реакции (E)',
                           'Двигательные реакции (M)',
                           'Стволовые рефлексы (B)',
                           'Дыхательный паттерн (R)',
                           'Интерпретация результата'],
        'part_name': '',
        'note': '',
        'type_table': 4,
        'type_result': 7
    },
    'Шкала моторного дефицита LAMS (Los Angeles Motor Scale)': {
        'sql': [MOTOR_DEFICIT_SCALE_FACIAL_ASYMMETRY_SQL,
                MOTOR_DEFICIT_SCALE_HOLDING_HANDS_SQL,
                MOTOR_DEFICIT_SCALE_SQUEEZING_BRUSH_SQL],
        'subtables_name': ['Ассиметрия лица',
                           'Удержание рук',
                           'Сжимание в кисти'],
        'part_name': 'Шкала моторного дефицита LAMS',
        'note': 'При угнетении уровня сознания до сопора или комы, баллы по шкале LAMS не определяются, указывается степень угнетения сознания (сопор, кома).',
        'type_table': 4,
        'type_result': 6
    }
}