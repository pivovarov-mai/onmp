import json

from config.utils import execute_sql

from dbsetter.medicines.request_medicines import (
    SHOW_ALL_MEDICINES,
    SHOW_MEDICINE_BY_ALL_NAME,
    SHOW_MEDICINE_BY_PART_NAME,
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


def peel_medicines(data):
    descriptions = [descr.name for descr in data[1]]

    '''
    "S. Urapidilum 5 mg/ml": {
        "S. Urapidili 5 mg/ml",
        "mg",
        "diagnoses": [
            "Тиреотоксический криз",
        ],
        "adult_dosages": [
            10.0,
        ]
        "child_dosages": [
            None,
        ]
        None,
        "contraindications": [
            <peel all>
        ]
    }
    '''
    result = {}

    for object in data[0]:
        name_of_med = object[0]
        if name_of_med not in result:
            result[name_of_med] = {}
            result[name_of_med]['genitive'] = object[1]
            result[name_of_med]['unit'] = object[2]
            result[name_of_med]['diagnoses'] = {}
            result[name_of_med]['diagnoses'][object[3]] = {
                'adult_dosages': object[4],
                'child_dosages': object[5],
                }
            # result[name_of_med]['adult_dosages'] = {object[4]}
            # result[name_of_med]['child_dosages'] = {object[5]}
            result[name_of_med]['child_dosage_unit'] = object[6]
            result[name_of_med]['contraindications'] = object[7].split(';')
        else:
            result[name_of_med]['diagnoses'][object[3]] = {
                'adult_dosages': object[4],
                'child_dosages': object[5],
            }

    print(len(result))
    return result
