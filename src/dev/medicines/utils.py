from config.utils import execute_sql

from dbsetter.medicines.request_medicines import (
    SHOW_ALL_MEDICINES,
    SHOW_MEDICINE_BY_ALL_NAME,
    SHOW_MEDICINE_BY_PART_NAME,
    SHOW_ALL_ADULT_MEDICINES,
    SHOW_ADULT_MEDICINE_BY_PART_NAME,
    SHOW_ALL_CHILD_MEDICINES,
    SHOW_CHILD_MEDICINE_BY_PART_NAME
)


# Get all medicines list with description
def get_all_medicines():
    return execute_sql(SHOW_ALL_MEDICINES)


# Get all medicines list with description by name
def get_medicines_by_name(name):
    return execute_sql(SHOW_MEDICINE_BY_ALL_NAME, [name])


# Get all medicines list with description by part of name
def get_medicines_by_part_of_name(part_of_name):
    return execute_sql(SHOW_MEDICINE_BY_PART_NAME, [f'%{part_of_name}%'])


# Get all medicines list with description by adult filter
def get_all_medicines_by_adult_filter():
    return execute_sql(SHOW_ALL_ADULT_MEDICINES)


# Get all medicines list with description by child filter
def get_all_medicines_by_child_filter():
    return execute_sql(SHOW_ALL_CHILD_MEDICINES)


# Get all medicines list with description by child filter by part of name
def get_all_medicines_by_part_of_name_by_adult_filter(part_name):
    return execute_sql(SHOW_ADULT_MEDICINE_BY_PART_NAME, [f'%{part_name}%'])


# Get all medicines list with description by child filter by part of name
def get_all_medicines_by_part_of_name_by_child_filter(part_name):
    return execute_sql(SHOW_CHILD_MEDICINE_BY_PART_NAME, [f'%{part_name}%'])


def peel_medicines_by_filters(data_adult, data_child):
    result = {}

    for object in data_adult[0]:
        name_of_med = object[0]
        if name_of_med not in result:
            result[name_of_med] = {}
            result[name_of_med]['genitive'] = object[1]
            result[name_of_med]['unit'] = object[2]
            result[name_of_med]['diagnoses'] = {}
            result[name_of_med]['diagnoses'][object[3]] = {
                'adult_dosage': object[4],
                'child_dosage': None
                }
            result[name_of_med]['contraindications'] = object[5].split(';')
        else:
            result[name_of_med]['diagnoses'][object[3]] = {
                'adult_dosage': object[4],
                'child_dosage': None
            }

    for object in data_child[0]:
        name_of_med = object[0]
        result[name_of_med]['child_dosage_unit'] = object[5]
        if object[3] in result[name_of_med]['diagnoses']:
            result[name_of_med]['diagnoses'][object[3]]['child_dosage'] = \
                object[4]
        else:
            result[name_of_med]['diagnoses'][object[3]] = {
                'adult_dosage': None,
                'child_dosage': object[4],
            }

    print(len(result))
    return result
