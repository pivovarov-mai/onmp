from config.utils import execute_sql

from django.core.cache import cache

from dbsetter.differential_diagnosis_tables.request_diff_diags import DATA

from config.loggers_conf import debug_log


# Saves all diags to cache for good performance
def cache_diags():
    summary_result = {}

    for item in DATA:
        current_check = DATA[item]
        current_data = {}

        # Parse sql
        if len(current_check['subtables_name']) == 0:  # We have zero subtables
            execution_result = execute_sql(current_check['sql'][0])
            execution_result_descr = [d.name for d in execution_result[1]]

            # Crutch for deleting id
            id_flag = False
            if execution_result_descr[0] == 'id':
                execution_result_descr = execution_result_descr[1:]
                id_flag = True

            current_data = []
            for record in execution_result[0]:

                # Crutch for deleting id in data
                record = record[id_flag:]

                current_data.append(
                    dict(zip(execution_result_descr, record))
                )
        else:  # We have some subtables
            for i, sql in enumerate(current_check['sql']):
                execution_result = execute_sql(sql)
                execution_result_descr = [d.name for d in execution_result[1]]

                # Crutch for deleting id
                id_flag = False
                if execution_result_descr[0] == 'id':
                    execution_result_descr = execution_result_descr[1:]
                    id_flag = True

                sub_name = current_check['subtables_name'][i]

                # Crutch for one table
                if item == "Шкала Глазго (Glasgow Coma Scale)" and \
                        sub_name != 'Интерпретация результата':
                    current_data[sub_name] = {}
                    for record in execution_result[0]:

                        # Crutch for deleting id in data
                        record = record[id_flag:]

                        action = record[0]
                        if action not in current_data[sub_name]:
                            current_data[sub_name][action] = []
                        current_data[sub_name][action].append({
                            'Ответ на действие': record[1],
                            'Балл': record[2],
                            })
                else:
                    current_data[sub_name] = []
                    for record in execution_result[0]:
                        
                        # Crutch for deleting id in data
                        record = record[id_flag:]

                        current_data[sub_name].append(
                            dict(zip(execution_result_descr, record)))

        summary_result[item] = {}
        summary_result[item]['data'] = current_data
        summary_result[item]['part_name'] = current_check['part_name']
        summary_result[item]['note'] = current_check['note']
        summary_result[item]['type_table'] = current_check['type_table']
        summary_result[item]['type_result'] = current_check['type_result']

    for i, item in enumerate(summary_result):
        cache.set(f'diags_{i}', {item: summary_result[item]}, None)

    cache.set('diags_all', summary_result, None)
    return summary_result


# Get all diags with cache using
def get_all_diags():
    result = cache.get('diags_all')
    if result is None:
        return cache_diags()
    return result


# Get all diags by name with cache using
def get_all_diags_by_name(name):
    try:
        ind = list(DATA.keys()).index(name)
    except Exception:
        raise ValueError(f'Unknown name: {name}')

    result = cache.get(f'diags_{ind}')
    if result is None:
        cache_diags()

    result = cache.get(f'diags_{ind}')
    if result is None:
        raise ValueError(f'Unknown name: {name} after cache')
    return result


def crunch_age(name, age):
    age = float(age)
    result = get_all_diags_by_name(name)
    age_column = ""
    if name == 'Определение площади ожогов у детей (по Lund и Browder)':
        if age < 1:
            age_column = "0 лет"
        elif age < 5:
            age_column = "1 год"
        elif age < 10:
            age_column = "5 лет"
        elif age < 15:
            age_column = "10 лет"
        elif age < 18:
            age_column = "15 лет"
        else:
            age_column = f"Возраст {age} не входит к диапазон 0-18"
    elif name == "Шкала Глазго (Glasgow Coma Scale)":
        if age < 1:
            age_column = "Грудные дети (до 1 года)"
        elif age < 4:
            age_column = "Дети от 1 до 4 лет"
        else:
            age_column = "Взрослые и дети старше 4 лет"
    else:
        age_column = f"{name} таблица не поддерживает возраст"
    result[name]['age_column'] = age_column
    return result
