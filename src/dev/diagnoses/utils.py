from config.utils import execute_sql


from dbsetter.diagnoses.request_diagnosis import (
    SHOW_DIAG_BY_ALL_CODE,
    SHOW_ALL_DIAG,
    SHOW_DIAG_BY_PART_CODE
)


# Get all diagnoses list with description
def get_all_diagnoses():
    return execute_sql(SHOW_ALL_DIAG)


# Get all diagnoses list with description by code
def get_diagnose_by_code(code: str):
    return execute_sql(SHOW_DIAG_BY_ALL_CODE, [code])


# Get all diagnoses list with description by part of code
def get_diagnose_by_part_code(part_code: str):
    return execute_sql(SHOW_DIAG_BY_PART_CODE, [f'%{part_code}%'])
