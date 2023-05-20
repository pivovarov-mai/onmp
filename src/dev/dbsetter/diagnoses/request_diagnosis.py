# Для Насти

# Поиск по полному соответствию названия кода МКБ
# По коду МКБ выводим все данные: а именно диагноз, рекомендации диагноза, тактику действий, его поддиагнозы, рекомендации поддиагноза и объем медицинской помощи диагноза или поддиагноза
# Возвращает список строк, которые соответствуют данному коду МКБ
# Принимает один параметр - код МКБ
# Возвращает 11 столбцов - 5 по которым сортим и 6 с данными
# mkb.id, diagnosis.id, sub_diagnosis.id, tactics.id, omp.id - id столбцов по которым сортим наши данные
# diagnosis.name_diagnosis - название диагноза
# diagnosis.recommendations_diagnosis - рекомендации диагноза
# tactics.name_tactics - тактика действий по определенному диагнозу
# sub_diagnosis.name_sub_diagnosis - название поддиагноза
# sub_diagnosis.recommendations_sub_diagnosis - рекомендации поддиагноза
# omp.name_omp - объем медицинской помощи диагноза или поддиагноза

SHOW_DIAG_BY_ALL_CODE = \
'''
SELECT DISTINCT mkb.id, diagnosis.id, sub_diagnosis.id, tactics.id, omp.id,
diagnosis.name_diagnosis, diagnosis.recommendations_diagnosis, tactics.name_tactics,
sub_diagnosis.name_sub_diagnosis, sub_diagnosis.recommendations_sub_diagnosis, omp.name_omp
FROM diagnosis
LEFT JOIN mkb_diagnosis ON diagnosis.id = mkb_diagnosis.diagnosis_id
LEFT JOIN mkb ON mkb.id = mkb_diagnosis.mkb_id
LEFT JOIN diagnosis_tactics ON diagnosis.id = diagnosis_tactics.diagnosis_id
LEFT JOIN tactics ON tactics.id = diagnosis_tactics.tactics_id
LEFT JOIN sub_diag_diagnosis ON diagnosis.id = sub_diag_diagnosis.diagnosis_id
LEFT JOIN sub_diagnosis ON sub_diagnosis.id = sub_diag_diagnosis.sub_diagnosis_id
LEFT JOIN sub_diagnosis_omp ON sub_diagnosis.id = sub_diagnosis_omp.sub_diagnosis_id
LEFT JOIN omp ON omp.id = sub_diagnosis_omp.omp_id
LEFT JOIN diagnosis_omp ON diagnosis.id = diagnosis_omp.diagnosis_id
WHERE mkb.name_mkb = %s
ORDER BY mkb.id ASC, diagnosis.id ASC, sub_diagnosis.id ASC, tactics.id ASC, omp.id ASC;
'''


# Вывод всех данных
# Выводим все данные для всех кодов МКБ: диагноз, рекомендации диагноза, тактику действий, его поддиагнозы, рекомендации поддиагноза и объем медицинской помощи диагноза или поддиагноза
# Возвращает список строк, которые соответствуют всем кодам МКБ
# Ничего не принимает
# Возвращает 12 столбцов - 5 по которым сортим и 7 с данными
# mkb.id, diagnosis.id, sub_diagnosis.id, tactics.id, omp.id - id столбцов по которым сортим наши данные
# mkb.name_mkb - название кода МКБ
# diagnosis.name_diagnosis - название диагноза
# diagnosis.recommendations_diagnosis - рекомендации диагноза
# tactics.name_tactics - тактика действий по определенному диагнозу
# sub_diagnosis.name_sub_diagnosis - название поддиагноза
# sub_diagnosis.recommendations_sub_diagnosis - рекомендации поддиагноза
# omp.name_omp - объем медицинской помощи диагноза или поддиагноза

SHOW_ALL_DIAG = \
'''
SELECT DISTINCT mkb.id, diagnosis.id, sub_diagnosis.id, tactics.id, omp.id,
mkb.name_mkb, diagnosis.name_diagnosis, diagnosis.recommendations_diagnosis, tactics.name_tactics,
sub_diagnosis.name_sub_diagnosis, sub_diagnosis.recommendations_sub_diagnosis, omp.name_omp
FROM diagnosis
LEFT JOIN mkb_diagnosis ON diagnosis.id = mkb_diagnosis.diagnosis_id
LEFT JOIN mkb ON mkb.id = mkb_diagnosis.mkb_id
LEFT JOIN diagnosis_tactics ON diagnosis.id = diagnosis_tactics.diagnosis_id
LEFT JOIN tactics ON tactics.id = diagnosis_tactics.tactics_id
LEFT JOIN sub_diag_diagnosis ON diagnosis.id = sub_diag_diagnosis.diagnosis_id
LEFT JOIN sub_diagnosis ON sub_diagnosis.id = sub_diag_diagnosis.sub_diagnosis_id
LEFT JOIN sub_diagnosis_omp ON sub_diagnosis.id = sub_diagnosis_omp.sub_diagnosis_id
LEFT JOIN omp ON omp.id = sub_diagnosis_omp.omp_id
LEFT JOIN diagnosis_omp ON diagnosis.id = diagnosis_omp.diagnosis_id
ORDER BY mkb.id ASC, diagnosis.id ASC, sub_diagnosis.id ASC, tactics.id ASC, omp.id ASC;
'''


# Поиск подстроки в строке
# По части кода МКБ выводим все данные, которые соответствую введенной подстроке: диагноз, рекомендации диагноза, тактику действий, его поддиагнозы, рекомендации поддиагноза и объем медицинской помощи диагноза или поддиагноза
# Возвращает список строк, которые соответствуют данной подстроке кода МКБ
# Принимает один параметр - подстрока кода МКБ
# Возвращает 11 столбцов - 5 по которым сортим и 6 с данными
# mkb.id, diagnosis.id, sub_diagnosis.id, tactics.id, omp.id - id столбцов по которым сортим наши данные
# diagnosis.name_diagnosis - название диагноза
# diagnosis.recommendations_diagnosis - рекомендации диагноза
# tactics.name_tactics - тактика действий по определенному диагнозу
# sub_diagnosis.name_sub_diagnosis - название поддиагноза
# sub_diagnosis.recommendations_sub_diagnosis - рекомендации поддиагноза
# omp.name_omp - объем медицинской помощи диагноза или поддиагноза

SHOW_DIAG_BY_PART_CODE = \
'''
SELECT DISTINCT mkb.id, diagnosis.id, sub_diagnosis.id, tactics.id, omp.id,
diagnosis.name_diagnosis, diagnosis.recommendations_diagnosis, tactics.name_tactics,
sub_diagnosis.name_sub_diagnosis, sub_diagnosis.recommendations_sub_diagnosis, omp.name_omp
FROM diagnosis
LEFT JOIN mkb_diagnosis ON diagnosis.id = mkb_diagnosis.diagnosis_id
LEFT JOIN mkb ON mkb.id = mkb_diagnosis.mkb_id
LEFT JOIN diagnosis_tactics ON diagnosis.id = diagnosis_tactics.diagnosis_id
LEFT JOIN tactics ON tactics.id = diagnosis_tactics.tactics_id
LEFT JOIN sub_diag_diagnosis ON diagnosis.id = sub_diag_diagnosis.diagnosis_id
LEFT JOIN sub_diagnosis ON sub_diagnosis.id = sub_diag_diagnosis.sub_diagnosis_id
LEFT JOIN sub_diagnosis_omp ON sub_diagnosis.id = sub_diagnosis_omp.sub_diagnosis_id
LEFT JOIN omp ON omp.id = sub_diagnosis_omp.omp_id
LEFT JOIN diagnosis_omp ON diagnosis.id = diagnosis_omp.diagnosis_id
WHERE mkb.name_mkb ILIKE %s
ORDER BY mkb.id ASC, diagnosis.id ASC, sub_diagnosis.id ASC, tactics.id ASC, omp.id ASC;
'''