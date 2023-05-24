У нас есть три таблицы cards, template и user_profile

Требуется сделать запросы по модели CRUD+L (Create, Read, Update, Delete + List)


# 1. Создание (Create):

# Создать новую карточку (card):

CREATE_NEW_CARD = \
'''
INSERT INTO cards (name, date, order, status, comment, account_user_id)
VALUES (%s, %s, %s, %s, %s, %s);
'''

# Создать новый профиль пользователя (user_profile):

CREATE_NEW_USER_PROFILE = \
'''
INSERT INTO user_profile (last_name, first_name, middle_name, date_of_birth, phone_number, passport, account_user_id)
VALUES (%s, %s, %s, %s, %s, %s, %s);
'''

# Создать новый шаблон (template):

CREATE_NEW_TEMPLATE = \
'''
INSERT INTO template (account_user_id, template_name, complaints, anamnesis, general_state, consciousness, position,
  position_text, skin, skin_text, rash, zev, tonsils, lymph_nodes, bedsores, edema, temperature,
  respiratory_rate, dyspnea, pathological_breathing, auscultatory, auscultatory_text, wheezing, wheezing_text,
  wet, wet_text, crepitus, percussion_sound, percussion_sound_text, cough, sputum, pulse, rhythmic_arrhythmic,
  filling, heart_rate, pulse_deficit, arterial_pressure, habitual, maximum, heart_sounds, noise_systolic_diasystolic,
  noise_on, held, accent, tone, tongue, tongue_text, belly_shape, tense, painful, painful_text, positive_symptoms,
  peristalsis, liver, spleen, vomit, feces, behavior, contact, sensitivity, speech, speech_text, pupils,
  photoreaction, nystagmus, facial_asymmetry, meningeal_symptoms, meningeal_symptoms_text, focal_symptoms,
  coordinator_samples, genitourinary_system, tapping_symptom, status_localis, instrumental_research, assistance,
  recommendations, signal_card, alcohol_wipes, shoe_covers, gloves, mask, hat, case, syringe2, syringe5, syringe10,
  syringe20, catheter, patch, scarif, test_strip, package, nebulizer_mask, date, order_number, checked)
VALUES (1, 'Новый шаблон', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
  NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
  NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
  NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
  NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
'''



# 2. Чтение (Read):

# Получить все карточки (cards):

READ_CARD = \
'''
SELECT *
FROM cards
WHERE id = %s;
'''

# Получить информацию о профиле пользователя с определенным идентификатором (user_profile):

READ_USER_PROFILE = \
'''
SELECT *
FROM user_profile
WHERE id = %s;
'''

# Получить все шаблоны (template):

READ_TEMPLATE = \
'''
SELECT *
FROM template
WHERE id = %s;
'''



# 3. Обновление (Update):

# Обновить информацию о карточке с определенным идентификатором (cards):

UPDATE_CARD = \
'''
UPDATE cards
SET name = %s, date = %s, order = %s, status = %s, comment = %s
WHERE id = %s;
'''

# Обновить информацию о профиле пользователя с определенным идентификатором (user_profile):

UPDATE_USER_PROFILE = \
'''
UPDATE user_profile
SET date_of_birth = %s, phone_number = %s, passport = %s
WHERE id = %s;
'''

# Обновить информацию о шаблоне с определенным идентификатором (template):

UPDATE_TEMPLATE = \
'''
UPDATE template
SET -------------------------------------
WHERE id = %s;
'''



# 4. Удаление (Delete):

# Удалить карточку с определенным идентификатором (cards):

DELETE_CARD = \
'''
DELETE FROM cards
WHERE id = %s;
'''

# Удалить профиль пользователя с определенным идентификатором (user_profile):

DELETE_USER_PROFILE = \
'''
DELETE FROM user_profile
WHERE id = %s;
'''

# Удалить шаблон с определенным идентификатором (template):

DELETE_TEMPLATE = \
'''
DELETE FROM template
WHERE id = %s;
'''



# 5. Вывод всего (List):

# Вывод всех карточек (cards):

SHOW_ALL_CARDS = \
'''
SELECT *
FROM cards
WHERE account_user_id = %s;
'''

# Вывод всех профилей пользователей (user_profile):

SHOW_ALL_USER_PROFILE = \
'''
SELECT * FROM user_profile;
'''

# Вывод всех шаблонов (template):

SHOW_ALL_TEMPLATE = \
'''
SELECT * FROM template WHERE account_user_id = %s;
'''