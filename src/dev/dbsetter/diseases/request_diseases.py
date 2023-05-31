# Для Даши

# Поиск по полному соответствию названия тега заболевания
# По тегу заболевания выводим все данные: заболевание, его описание, его период, его симптомы, формы заболевания, описание формы заболевания и симптомы форм заболевания.
# Возвращает список строк, которые соответствуют данному названию раздела
# Принимает один параметр - тег заболевания
# Возвращает 10 столбцов - 3 по которым сортим и 7 с данными
# diseases.id, disease_symptoms.id, form_symptoms.id - id столбцов по которым сортим наши данные
# diseases.name - название заболевания
# diseases.description - описание заболевания
# diseases.period - период заболевания
# disease_symptoms.name - симптомы заболевания
# form_disease.name - формы заболевания
# form_disease.description - описание формы заболевания
# form_symptoms.name - симптомы формы заболевания

SHOW_DISEASES_BY_ALL_TAG = \
'''
SELECT DISTINCT diseases.id, disease_symptoms.id, form_symptoms.id,
diseases.name AS "Заболевание", diseases.description AS "Описание заболевания", diseases.period AS "Период заболевания", disease_symptoms.name AS "Симптомы заболевания", form_disease.name AS "Формы заболевания", form_disease.description AS "Описание формы заболевания", form_symptoms.name AS "Симптомы формы заболевания"
FROM diseases
JOIN disease_tags ON diseases.tag_id = disease_tags.id
LEFT JOIN diseases_disease_symptoms ON diseases.id = diseases_disease_symptoms.diseases_id
LEFT JOIN disease_symptoms ON diseases_disease_symptoms.symptom_diseases_id = disease_symptoms.id
LEFT JOIN diseases_form_disease ON diseases.id = diseases_form_disease.diseases_id
LEFT JOIN form_disease ON diseases_form_disease.form_id = form_disease.id
LEFT JOIN form_disease_form_symptoms ON form_disease.id = form_disease_form_symptoms.form_id
LEFT JOIN form_symptoms ON form_disease_form_symptoms.symptom_form_id = form_symptoms.id
WHERE disease_tags.name_tag = %s
ORDER BY diseases.id ASC, disease_symptoms.id ASC, form_symptoms.id ASC;
'''


# Вывод всех данных
# Выводим все данные для всех заболеваний: заболевание, его описание, его период, его симптомы, формы заболевания, описание формы заболевания и симптомы форм заболевания.
# Возвращает список строк, которые соответствуют всем тегам заболевания
# Ничего не принимает
# Возвращает 11 столбцов - 3 по которым сортим и 8 с данными
# diseases.id, disease_symptoms.id, form_symptoms.id - id столбцов по которым сортим наши данные
# disease_tags.name_tag - название тега заболевания
# diseases.name - название заболевания
# diseases.description - описание заболевания
# diseases.period - период заболевания 	
# disease_symptoms.name - симптомы заболевания
# form_disease.name - формы заболевания
# form_disease.description - описание формы заболевания
# form_symptoms.name - симптомы формы заболевания

SHOW_ALL_DISEASES = \
'''
SELECT DISTINCT diseases.id, disease_symptoms.id, form_symptoms.id,
disease_tags.name_tag AS "Тег заболевания", diseases.name AS "Заболевание", diseases.description AS "Описание заболевания", diseases.period AS "Период заболевания", disease_symptoms.name AS "Симптомы заболевания", form_disease.name AS "Формы заболевания", form_disease.description AS "Описание формы заболевания", form_symptoms.name AS "Симптомы формы заболевания"
FROM diseases
JOIN disease_tags ON diseases.tag_id = disease_tags.id
LEFT JOIN diseases_disease_symptoms ON diseases.id = diseases_disease_symptoms.diseases_id
LEFT JOIN disease_symptoms ON diseases_disease_symptoms.symptom_diseases_id = disease_symptoms.id
LEFT JOIN diseases_form_disease ON diseases.id = diseases_form_disease.diseases_id
LEFT JOIN form_disease ON diseases_form_disease.form_id = form_disease.id
LEFT JOIN form_disease_form_symptoms ON form_disease.id = form_disease_form_symptoms.form_id
LEFT JOIN form_symptoms ON form_disease_form_symptoms.symptom_form_id = form_symptoms.id
ORDER BY diseases.id ASC, disease_symptoms.id ASC, form_symptoms.id ASC;
'''


# По части тега заболевания выводим все данные, которые соответствую введенной подстроке: заболевание, его описание, его период, его симптомы, формы заболевания, описание формы заболевания и симптомы форм заболевания.
# Возвращает список строк, которые соответствуют данному названию раздела
# Принимает один параметр - подстрока тега заболевания
# Возвращает 10 столбцов - 3 по которым сортим и 7 с данными
# diseases.id, disease_symptoms.id, form_symptoms.id - id столбцов по которым сортим наши данные
# diseases.name - название заболевания
# diseases.description - описание заболевания
# diseases.period - период заболевания
# disease_symptoms.name - симптомы заболевания
# form_disease.name - формы заболевания
# form_disease.description - описание формы заболевания
# form_symptoms.name - симптомы формы заболевания

SHOW_DISEASES_BY_PART_CODE = \
'''
SELECT DISTINCT diseases.id, disease_symptoms.id, form_symptoms.id,
diseases.name AS "Заболевание", diseases.description AS "Описание заболевания", diseases.period AS "Период заболевания", disease_symptoms.name AS "Симптомы заболевания", form_disease.name AS "Формы заболевания", form_disease.description AS "Описание формы заболевания", form_symptoms.name AS "Симптомы формы заболевания"
FROM diseases
JOIN disease_tags ON diseases.tag_id = disease_tags.id
LEFT JOIN diseases_disease_symptoms ON diseases.id = diseases_disease_symptoms.diseases_id
LEFT JOIN disease_symptoms ON diseases_disease_symptoms.symptom_diseases_id = disease_symptoms.id
LEFT JOIN diseases_form_disease ON diseases.id = diseases_form_disease.diseases_id
LEFT JOIN form_disease ON diseases_form_disease.form_id = form_disease.id
LEFT JOIN form_disease_form_symptoms ON form_disease.id = form_disease_form_symptoms.form_id
LEFT JOIN form_symptoms ON form_disease_form_symptoms.symptom_form_id = form_symptoms.id
WHERE disease_tags.name_tag ILIKE %s
ORDER BY diseases.id ASC, disease_symptoms.id ASC, form_symptoms.id ASC;
'''


# -----------------------------------------------------------------------------------------------

# Поиск по полному соответствию названия заболевания
# По названию заболевания выводим все данные: заболевание, его описание, его период, его симптомы, формы заболевания, описание формы заболевания и симптомы форм заболевания.
# Возвращает список строк, которые соответствуют данному названию заболевания
# Принимает один параметр - название заболевания
# Возвращает 10 столбцов - 3 по которым сортим и 7 с данными
# diseases.id, disease_symptoms.id, form_symptoms.id - id столбцов по которым сортим наши данные
# diseases.name - название заболевания
# diseases.description - описание заболевания
# diseases.period - период заболевания
# disease_symptoms.name - симптомы заболевания
# form_disease.name - формы заболевания
# form_disease.description - описание формы заболевания
# form_symptoms.name - симптомы формы заболевания

SHOW_DISEASES_BY_ALL_NAME = \
'''
SELECT DISTINCT diseases.id, disease_symptoms.id, form_symptoms.id,
disease_tags.name_tag AS "Тег заболевания", diseases.name AS "Заболевание", diseases.description AS "Описание заболевания", diseases.period AS "Период заболевания", disease_symptoms.name AS "Симптомы заболевания", form_disease.name AS "Формы заболевания", form_disease.description AS "Описание формы заболевания", form_symptoms.name AS "Симптомы формы заболевания"
FROM diseases
JOIN disease_tags ON diseases.tag_id = disease_tags.id
LEFT JOIN diseases_disease_symptoms ON diseases.id = diseases_disease_symptoms.diseases_id
LEFT JOIN disease_symptoms ON diseases_disease_symptoms.symptom_diseases_id = disease_symptoms.id
LEFT JOIN diseases_form_disease ON diseases.id = diseases_form_disease.diseases_id
LEFT JOIN form_disease ON diseases_form_disease.form_id = form_disease.id
LEFT JOIN form_disease_form_symptoms ON form_disease.id = form_disease_form_symptoms.form_id
LEFT JOIN form_symptoms ON form_disease_form_symptoms.symptom_form_id = form_symptoms.id
WHERE diseases.name = %s
ORDER BY diseases.id ASC, disease_symptoms.id ASC, form_symptoms.id ASC;
'''

# По части названия заболевания выводим все данные, которые соответствую введенной подстроке: заболевание, его описание, его период, его симптомы, формы заболевания, описание формы заболевания и симптомы форм заболевания.
# Возвращает список строк, которые соответствуют данному названию заболевания
# Принимает один параметр - подстрока названия заболевания
# Возвращает 10 столбцов - 3 по которым сортим и 7 с данными
# diseases.id, disease_symptoms.id, form_symptoms.id - id столбцов по которым сортим наши данные
# diseases.name - название заболевания
# diseases.description - описание заболевания
# diseases.period - период заболевания
# disease_symptoms.name - симптомы заболевания
# form_disease.name - формы заболевания
# form_disease.description - описание формы заболевания
# form_symptoms.name - симптомы формы заболевания

SHOW_DISEASES_BY_PART_NAME = \
'''
SELECT DISTINCT diseases.id, disease_symptoms.id, form_symptoms.id,
disease_tags.name_tag AS "Тег заболевания", diseases.name AS "Заболевание", diseases.description AS "Описание заболевания", diseases.period AS "Период заболевания", disease_symptoms.name AS "Симптомы заболевания", form_disease.name AS "Формы заболевания", form_disease.description AS "Описание формы заболевания", form_symptoms.name AS "Симптомы формы заболевания"
FROM diseases
JOIN disease_tags ON diseases.tag_id = disease_tags.id
LEFT JOIN diseases_disease_symptoms ON diseases.id = diseases_disease_symptoms.diseases_id
LEFT JOIN disease_symptoms ON diseases_disease_symptoms.symptom_diseases_id = disease_symptoms.id
LEFT JOIN diseases_form_disease ON diseases.id = diseases_form_disease.diseases_id
LEFT JOIN form_disease ON diseases_form_disease.form_id = form_disease.id
LEFT JOIN form_disease_form_symptoms ON form_disease.id = form_disease_form_symptoms.form_id
LEFT JOIN form_symptoms ON form_disease_form_symptoms.symptom_form_id = form_symptoms.id
WHERE diseases.name ILIKE %s
ORDER BY diseases.id ASC, disease_symptoms.id ASC, form_symptoms.id ASC;
'''
