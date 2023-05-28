# Для Маши

# Поиск по полному соответствию названия препарата
# По названию препарата выводим все данные: название препарата, его противопоказания, взрослую и детские дозировки в зависимости от диагноза
# Возвращает список строк, которые соответствуют данному препарату
# Принимает один параметр - название препарата 
# Возвращает 8 столбцов с данными
# medicines.name - название препарата
# medicines.name_genitive - название препарата в родительном падеже
# medicines.unit - мера препарата
# contraindications.name - противопоказания препарата
# diag.name - название диагноза
# adult_dosages.dosage - взрослая дозировка
# child_dosages.dosage - детская дозировка
# child_dosages.unit - мера детской дозировки

SHOW_MEDICINE_BY_ALL_NAME = \
'''
SELECT DISTINCT medicines.name AS "Название медикамента Им.п.", medicines.name_genitive AS "Название медикамента Р.п.", medicines.unit AS "Мера медикамента",diag.name AS "Название диагноза", adult_dosages.dosage AS "Взрослая дозировка", child_dosages.dosage AS "Детская дозировка", child_dosages.unit AS "Мера детской дозировки", contraindications.name AS "Противопоказания"
FROM medicines
LEFT JOIN medicines_contraindications ON medicines.id = medicines_contraindications.medicines_id
LEFT JOIN contraindications ON contraindications.id = medicines_contraindications.contraindication_id 
LEFT JOIN adult_dosages ON medicines.id = adult_dosages.medicines_id
LEFT JOIN child_dosages ON medicines.id = child_dosages.medicines_id
LEFT JOIN diag ON adult_dosages.diag_id = diag.id OR child_dosages.diag_id = diag.id
WHERE medicines.name = %s
ORDER BY medicines.name ASC, contraindications.name ASC, diag.name ASC;
'''

# Вывод всех данных
# Выводим все данные для всех препаратов: название препарата, его противопоказания, взрослую и детские дозировки в зависимости от диагноза
# Возвращает список строк, которые соответствуют всем препаратам
# Ничего не принимает
# Возвращает 8 столбцов с данными
# medicines.name - название препарата
# medicines.name_genitive - название препарата в родительном падеже
# medicines.unit - мера препарата
# contraindications.name - противопоказания препарата
# diag.name - название диагноза
# adult_dosages.dosage - взрослая дозировка
# child_dosages.dosage - детская дозировка
# child_dosages.unit - мера детской дозировки

SHOW_ALL_MEDICINES = \
'''
SELECT DISTINCT medicines.name AS "Название медикамента Им.п.", medicines.name_genitive AS "Название медикамента Р.п.", medicines.unit AS "Мера медикамента",diag.name AS "Название диагноза", adult_dosages.dosage AS "Взрослая дозировка", child_dosages.dosage AS "Детская дозировка", child_dosages.unit AS "Мера детской дозировки", contraindications.name AS "Противопоказания"
FROM medicines
LEFT JOIN medicines_contraindications ON medicines.id = medicines_contraindications.medicines_id
LEFT JOIN contraindications ON contraindications.id = medicines_contraindications.contraindication_id 
LEFT JOIN adult_dosages ON medicines.id = adult_dosages.medicines_id
LEFT JOIN child_dosages ON medicines.id = child_dosages.medicines_id
LEFT JOIN diag ON adult_dosages.diag_id = diag.id OR child_dosages.diag_id = diag.id
ORDER BY medicines.name ASC, contraindications.name ASC, diag.name ASC;
'''

# Поиск подстроки в строке
# По части названия препарата выводим все данные, которые соответствую введенной подстроке: название препарата, его противопоказания, взрослую и детские дозировки в зависимости от диагноза
# Возвращает список строк, которые соответствуют данной подстроке названия препарата
# Принимает один параметр - подстрока названия препарата
# Возвращает 8 столбцов с данными
# medicines.name - название препарата
# medicines.name_genitive - название препарата в родительном падеже
# medicines.unit - мера препарата
# contraindications.name - противопоказания препарата
# diag.name - название диагноза
# adult_dosages.dosage - взрослая дозировка
# child_dosages.dosage - детская дозировка
# child_dosages.unit - мера детской дозировки

SHOW_MEDICINE_BY_PART_NAME = \
'''
SELECT DISTINCT medicines.name AS "Название медикамента Им.п.", medicines.name_genitive AS "Название медикамента Р.п.", medicines.unit AS "Мера медикамента",diag.name AS "Название диагноза", adult_dosages.dosage AS "Взрослая дозировка", child_dosages.dosage AS "Детская дозировка", child_dosages.unit AS "Мера детской дозировки", contraindications.name AS "Противопоказания"
FROM medicines
LEFT JOIN medicines_contraindications ON medicines.id = medicines_contraindications.medicines_id
LEFT JOIN contraindications ON contraindications.id = medicines_contraindications.contraindication_id 
LEFT JOIN adult_dosages ON medicines.id = adult_dosages.medicines_id
LEFT JOIN child_dosages ON medicines.id = child_dosages.medicines_id
LEFT JOIN diag ON adult_dosages.diag_id = diag.id OR child_dosages.diag_id = diag.id
WHERE medicines.name ILIKE %s
ORDER BY medicines.name ASC, contraindications.name ASC, diag.name ASC;
'''