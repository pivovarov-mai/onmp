EXAMPLE_WITHOUR_PARAMETERS = 'SELECT id, first_name, last_name, birth_date FROM my_table'

EXAMPLE_WITHOUT_PARAMETERS_BUT_MULTIPLE = \
'''
SELECT id, first_name as imya
FROM some_table
'''

# Первый параметр принимает кол-во лет, а второй имя кошки
# Возвращает список пользователей, которые соответствуют требованиям выше
EXAMPLE_REQUEST_WITH_LIST_PARAMS = \
'''
SELECT * from users 
where id = %s and
city = %s and 
state = %s
'''

EXAMPLE_REQUEST_WITH_DICT_PARAMS = \
'''
SELECT * from users 
where id = %(id)s and
city = %(city)s and 
state = %(state)s 
'''