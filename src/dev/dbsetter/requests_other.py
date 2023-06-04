# У нас есть три таблицы cards, template и user_profile
# Требуется сделать запросы по модели CRUD+L (Create, Read, Update, Delete + List)


# 1. Создание (Create):

# Создать новую карточку (card):

CREATE_NEW_CARD = \
'''
INSERT INTO cards ("name", "date", "order", "status", "comment", "account_user_id")
VALUES (%(name)s, %(date)s, %(order)s, %(status)s, %(comment)s, %(account_user_id)s)
RETURNING id;
'''

# Создать новый профиль пользователя (user_profile):

CREATE_NEW_USER_PROFILE = \
'''
INSERT INTO user_profile ("last_name", "first_name", "middle_name", "date_of_birth", "phone_number", "passport", "account_user_id")
VALUES (%(last_name)s, %(first_name)s, %(middle_name)s, %(date_of_birth)s, %(phone_number)s, %(passport)s, %(account_user_id)s)
RETURNING id;
'''

# Создать новый шаблон (template):

CREATE_NEW_TEMPLATE = \
'''
INSERT INTO "template" (
  "account_user_id", "template_name", "complaints", "anamnesis", "general_state",
  "consciousness", "position", "position_text", "skin", "skin_text",
  "rash", "zev", "tonsils", "lymph_nodes", "bedsores",
  "edema", "temperature", "respiratory_rate", "dyspnea", "pathological_breathing",
  "auscultatory", "auscultatory_text", "wheezing", "wheezing_text", "wet",
  "wet_text", "crepitus", "percussion_sound", "percussion_sound_text", "cough",
  "sputum", "pulse", "rhythmic_arrhythmic", "filling", "heart_rate",
  "pulse_deficit", "arterial_pressure", "habitual", "maximum", "heart_sounds",
  "noise_systolic_diasystolic", "noise_on", "held", "accent", "tone",
  "tongue", "tongue_text", "belly_shape", "tense", "painful",
  "painful_text", "positive_symptoms", "peristalsis", "liver", "spleen",
  "vomit", "feces", "behavior", "contact", "sensitivity",
  "speech", "speech_text", "pupils", "photoreaction", "nystagmus",
  "facial_asymmetry", "meningeal_symptoms", "meningeal_symptoms_text", "focal_symptoms", "coordinator_samples",
  "genitourinary_system", "tapping_symptom", "status_localis", "instrumental_research", "assistance",
  "recommendations", "signal_card", "alcohol_wipes", "shoe_covers", "gloves",
  "mask", "hat", "case", "syringe2", "syringe5",
  "syringe10", "syringe20", "catheter", "patch", "scarif",
  "test_strip", "package", "nebulizer_mask", "date", "order_number", "checked")
VALUES (
  %(account_user_id)s, %(template_name)s, %(complaints)s, %(anamnesis)s, %(general_state)s,
  %(consciousness)s, %(position)s, %(position_text)s, %(skin)s, %(skin_text)s,
  %(rash)s, %(zev)s, %(tonsils)s, %(lymph_nodes)s, %(bedsores)s,
  %(edema)s, %(temperature)s, %(respiratory_rate)s, %(dyspnea)s, %(pathological_breathing)s,
  %(auscultatory)s, %(auscultatory_text)s, %(wheezing)s, %(wheezing_text)s, %(wet)s,
  %(wet_text)s, %(crepitus)s, %(percussion_sound)s, %(percussion_sound_text)s, %(cough)s,
  %(sputum)s, %(pulse)s, %(rhythmic_arrhythmic)s, %(filling)s, %(heart_rate)s,
  %(pulse_deficit)s, %(arterial_pressure)s, %(habitual)s, %(maximum)s, %(heart_sounds)s,
  %(noise_systolic_diasystolic)s, %(noise_on)s, %(held)s, %(accent)s, %(tone)s,
  %(tongue)s, %(tongue_text)s, %(belly_shape)s, %(tense)s, %(painful)s,
  %(painful_text)s, %(positive_symptoms)s, %(peristalsis)s, %(liver)s, %(spleen)s,
  %(vomit)s, %(feces)s, %(behavior)s, %(contact)s, %(sensitivity)s,
  %(speech)s, %(speech_text)s, %(pupils)s, %(photoreaction)s, %(nystagmus)s,
  %(facial_asymmetry)s, %(meningeal_symptoms)s, %(meningeal_symptoms_text)s, %(focal_symptoms)s, %(coordinator_samples)s,
  %(genitourinary_system)s, %(tapping_symptom)s, %(status_localis)s, %(instrumental_research)s, %(assistance)s,
  %(recommendations)s, %(signal_card)s, %(alcohol_wipes)s, %(shoe_covers)s, %(gloves)s,
  %(mask)s, %(hat)s, %(case)s, %(syringe2)s, %(syringe5)s,
  %(syringe10)s, %(syringe20)s, %(catheter)s, %(patch)s, %(scarif)s,
  %(test_strip)s, %(package)s, %(nebulizer_mask)s, %(date)s, %(order_number)s, %(checked)s
RETURNING id;
'''


# 2. Чтение (Read):

# Получить все карточки (cards):

READ_CARD = \
'''
SELECT * FROM cards
WHERE id = %(id)s;
'''

# Получить информацию о профиле пользователя с определенным идентификатором (user_profile):

READ_USER_PROFILE = \
'''
SELECT * FROM user_profile
WHERE account_user_id = %(account_user_id)s;
'''

# Получить все шаблоны (template):

READ_TEMPLATE = \
'''
SELECT * FROM template
WHERE id = %(id)s;
'''



# 3. Обновление (Update):

# Обновить информацию о карточке с определенным идентификатором (cards):

UPDATE_CARD = \
'''
UPDATE cards
SET "name" = %(name)s,
    "date" = %(date)s,
    "order" = %(order)s,
    "status" = %(status)s,
    "comment" = %(comment)s
WHERE id = %(id)s;
'''

# Обновить информацию о профиле пользователя с определенным идентификатором (user_profile):

UPDATE_USER_PROFILE = \
'''
UPDATE user_profile
SET "last_name" = %(last_name)s,
    "first_name" = %(first_name)s,
    "middle_name" = %(middle_name)s,
    "date_of_birth" = %(date_of_birth)s,
    "phone_number" = %(phone_number)s,
    "passport" = %(passport)s
WHERE account_user_id = %(account_user_id)s;
'''

# Обновить информацию о шаблоне с определенным идентификатором (template):

UPDATE_TEMPLATE = \
'''
UPDATE template
SET
  "account_user_id" = %(account_user_id)s, "template_name" = %(template_name)s, "complaints" = %(complaints)s, "anamnesis" = %(anamnesis)s, "general_state" = %(general_state)s,
  "consciousness" = %(consciousness)s, "position" = %(position)s, "position_text" = %(position_text)s, "skin" = %(skin)s, "skin_text" = %(skin_text)s,
  "rash" = %(rash)s, "zev" = %(zev)s, "tonsils" = %(tonsils)s, "lymph_nodes" = %(lymph_nodes)s, "bedsores" = %(bedsores)s,
  "edema" = %(edema)s, "temperature" = %(temperature)s, "respiratory_rate" = %(respiratory_rate)s, "dyspnea" = %(dyspnea)s, "pathological_breathing" = %(pathological_breathing)s,
  "auscultatory" = %(auscultatory)s, "auscultatory_text" = %(auscultatory_text)s, "wheezing" = %(wheezing)s, "wheezing_text" = %(wheezing_text)s, "wet" = %(wet)s,
  "wet_text" = %(wet_text)s, "crepitus" = %(crepitus)s, "percussion_sound" = %(percussion_sound)s, "percussion_sound_text" = %(percussion_sound_text)s, "cough" = %(cough)s,
  "sputum" = %(sputum)s, "pulse" = %(pulse)s, "rhythmic_arrhythmic" = %(rhythmic_arrhythmic)s, "filling" = %(filling)s, "heart_rate" = %(heart_rate)s,
  "pulse_deficit" = %(pulse_deficit)s, "arterial_pressure" = %(arterial_pressure)s, "habitual" = %(habitual)s, "maximum" = %(maximum)s, "heart_sounds" = %(heart_sounds)s,
  "noise_systolic_diasystolic" = %(noise_systolic_diasystolic)s, "noise_on" = %(noise_on)s, "held" = %(held)s, "accent" = %(accent)s, "tone" = %(tone)s,
  "tongue" = %(tongue)s, "tongue_text" = %(tongue_text)s, "belly_shape" = %(belly_shape)s, "tense" = %(tense)s, "painful" = %(painful)s,
  "painful_text" = %(painful_text)s, "positive_symptoms" = %(positive_symptoms)s, "peristalsis" = %(peristalsis)s, "liver" = %(liver)s, "spleen" = %(spleen)s,
  "vomit" = %(vomit)s, "feces" = %(feces)s, "behavior" = %(behavior)s, "contact" = %(contact)s, "sensitivity" = %(sensitivity)s,
  "speech" = %(speech)s, "speech_text" = %(speech_text)s, "pupils" = %(pupils)s, "photoreaction" = %(photoreaction)s, "nystagmus" = %(nystagmus)s,
  "facial_asymmetry" = %(facial_asymmetry)s, "meningeal_symptoms" = %(meningeal_symptoms)s, "meningeal_symptoms_text" = %(meningeal_symptoms_text)s, "focal_symptoms" = %(focal_symptoms)s, "coordinator_samples" = %(coordinator_samples)s,
  "genitourinary_system" = %(genitourinary_system)s, "tapping_symptom" = %(tapping_symptom)s, "status_localis" = %(status_localis)s, "instrumental_research" = %(instrumental_research)s, "assistance" = %(assistance)s,
  "recommendations" = %(recommendations)s, "signal_card" = %(signal_card)s, "alcohol_wipes" = %(alcohol_wipes)s, "shoe_covers" = %(shoe_covers)s, "gloves" = %(gloves)s,
  "mask" = %(mask)s, "hat" = %(hat)s, "case" = %(case)s, "syringe2" = %(syringe2)s, "syringe5" = %(syringe5)s,
  "syringe10" = %(syringe10)s, "syringe20" = %(syringe20)s, "catheter" = %(catheter)s, "patch" = %(patch)s, "scarif" = %(scarif)s,
  "test_strip" = %(test_strip)s, "package" = %(package)s, "nebulizer_mask" = %(nebulizer_mask)s, "date" = %(date)s, "order_number" = %(order_number)s, "checked" = %(checked)s
WHERE id = %(id)s;
'''



# 4. Удаление (Delete):

# Удалить карточку с определенным идентификатором (cards):

DELETE_CARD = \
'''
DELETE FROM cards
WHERE id = %(id)s;
'''

# Удалить профиль пользователя с определенным идентификатором (user_profile):

DELETE_USER_PROFILE = \
'''
DELETE FROM user_profile
WHERE account_user_id = %(account_user_id)s;
'''

# Удалить шаблон с определенным идентификатором (template):

DELETE_TEMPLATE = \
'''
DELETE FROM template
WHERE id = %(id)s;
'''



# 5. Вывод всего (List):

# Вывод всех карточек (cards):

SHOW_ALL_CARDS = \
'''
SELECT * FROM cards
WHERE account_user_id = %(account_user_id)s;
'''

# Вывод всех профилей пользователей (user_profile):

SHOW_ALL_USER_PROFILE = \
'''
SELECT * FROM user_profile;
'''

# Вывод всех шаблонов (template):

SHOW_ALL_TEMPLATE = \
'''
SELECT * FROM template
WHERE account_user_id = %(account_user_id)s;
'''
