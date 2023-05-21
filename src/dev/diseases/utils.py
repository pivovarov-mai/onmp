from config.utils import execute_sql
from dbsetter.diseases.request_diseases import (
    SHOW_ALL_DISEASES,
    SHOW_DISEASE_BY_ALL_TAG,
    SHOW_DIAG_BY_PART_CODE
)


# Get all diseases list with description
def get_all_diseases():
    return execute_sql(SHOW_ALL_DISEASES)


# Get all diseases list with description by tag
def get_diseases_by_tag(tag):
    return execute_sql(SHOW_DISEASE_BY_ALL_TAG, [tag])


# Get all diagnoses list with description by part of code
def get_diseases_by_part_of_tag(part_of_tag):
    return execute_sql(SHOW_DIAG_BY_PART_CODE, [f'%{part_of_tag}%'])
