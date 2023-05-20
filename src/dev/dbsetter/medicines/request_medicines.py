# Для Маши

# Поиск по полному соответствию названия препарата
# По названию препарата выводим все данные: название препарата, его противопоказания, взрослую и детские дозировки в зависимости от диагноза
# Возвращает список строк, которые соответствуют данному препарату
# Принимает один параметр - название препарата 
# Возвращает 8 столбцов с данными
# medicines.name_medicine - название препарата
# medicines.name_medicine_genitive - название препарата в родительном падеже
# medicines.unit_medicine - мера препарата
# contraindications.name_contraindication - противопоказания препарата
# diag.name_diag - название диагноза
# adult_dosages.adult_dosage - взрослая дозировка
# child_dosages.hild_dosage - детская дозировка
# child_dosages.unit_child_dosage - мера детской дозировки

SHOW_MEDICINE_BY_ALL_NAME = \
'''
SELECT DISTINCT medicines.name_medicine, medicines.name_medicine_genitive, medicines.unit_medicine, contraindications.name_contraindication,
diag.name_diag, adult_dosages.adult_dosage, child_dosages.child_dosage, child_dosages.unit_child_dosage 
FROM medicines
LEFT JOIN medicines_contraindications ON medicines.id = medicines_contraindications.medicines_id
LEFT JOIN contraindications ON contraindications.id = medicines_contraindications.contraindication_id 
LEFT JOIN adult_dosages ON medicines.id = adult_dosages.medicines_id
LEFT JOIN child_dosages ON medicines.id = child_dosages.medicines_id
LEFT JOIN diag ON adult_dosages.diag_id = diag.id OR child_dosages.diag_id = diag.id
WHERE medicines.name_medicine = %s
ORDER BY medicines.name_medicine ASC, contraindications.name_contraindication ASC, diag.name_diag ASC;
'''

# Вывод всех данных
# Выводим все данные для всех препаратов: название препарата, его противопоказания, взрослую и детские дозировки в зависимости от диагноза
# Возвращает список строк, которые соответствуют всем препаратам
# Ничего не принимает
# Возвращает 8 столбцов с данными
# medicines.name_medicine - название препарата
# medicines.name_medicine_genitive - название препарата в родительном падеже
# medicines.unit_medicine - мера препарата
# contraindications.name_contraindication - противопоказания препарата
# diag.name_diag - название диагноза
# adult_dosages.adult_dosage - взрослая дозировка
# child_dosages.hild_dosage - детская дозировка
# child_dosages.unit_child_dosage - мера детской дозировки

SHOW_ALL_MEDICINES = \
'''
SELECT DISTINCT medicines.name_medicine, medicines.name_medicine_genitive, medicines.unit_medicine, contraindications.name_contraindication,
diag.name_diag, adult_dosages.adult_dosage, child_dosages.child_dosage, child_dosages.unit_child_dosage
FROM medicines
LEFT JOIN medicines_contraindications ON medicines.id = medicines_contraindications.medicines_id
LEFT JOIN contraindications ON contraindications.id = medicines_contraindications.contraindication_id 
LEFT JOIN adult_dosages ON medicines.id = adult_dosages.medicines_id
LEFT JOIN child_dosages ON medicines.id = child_dosages.medicines_id
LEFT JOIN diag ON adult_dosages.diag_id = diag.id OR child_dosages.diag_id = diag.id
ORDER BY medicines.name_medicine ASC, contraindications.name_contraindication ASC, diag.name_diag ASC;
'''

# Поиск подстроки в строке
# По части названия препарата выводим все данные, которые соответствую введенной подстроке: название препарата, его противопоказания, взрослую и детские дозировки в зависимости от диагноза
# Возвращает список строк, которые соответствуют данной подстроке названия препарата
# Принимает один параметр - подстрока названия препарата
# Возвращает 8 столбцов с данными
# medicines.name_medicine - название препарата
# medicines.name_medicine_genitive - название препарата в родительном падеже
# medicines.unit_medicine - мера препарата
# contraindications.name_contraindication - противопоказания препарата
# diag.name_diag - название диагноза
# adult_dosages.adult_dosage - взрослая дозировка
# child_dosages.hild_dosage - детская дозировка
# child_dosages.unit_child_dosage - мера детской дозировки

SHOW_MEDICINE_BY_PART_NAME = \
'''
SELECT DISTINCT medicines.name_medicine, medicines.name_medicine_genitive, medicines.unit_medicine, contraindications.name_contraindication,
diag.name_diag, adult_dosages.adult_dosage, child_dosages.child_dosage, child_dosages.unit_child_dosage
FROM medicines
LEFT JOIN medicines_contraindications ON medicines.id = medicines_contraindications.medicines_id
LEFT JOIN contraindications ON contraindications.id = medicines_contraindications.contraindication_id 
LEFT JOIN adult_dosages ON medicines.id = adult_dosages.medicines_id
LEFT JOIN child_dosages ON medicines.id = child_dosages.medicines_id
LEFT JOIN diag ON adult_dosages.diag_id = diag.id OR child_dosages.diag_id = diag.id
WHERE medicines.name_medicine ILIKE %s
ORDER BY medicines.name_medicine ASC, contraindications.name_contraindication ASC, diag.name_diag ASC;
'''