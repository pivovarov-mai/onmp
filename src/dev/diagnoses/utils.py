from config.utils import execute_sql

from django.core.cache import cache

from dbsetter.diagnoses.request_diagnosis import (
    SHOW_ONLY_DIAG_BY_PART_CODE,
    SHOW_ONLY_PODDIAG_BY_PART_CODE,
    SHOW_ONLY_ALL_DIAG,
    SHOW_ONLY_ALL_SUBDIAG,
)


# Get all separated diagnoses and subdiagnoses
def get_all_separated_diagnoses():
    result = execute_sql(SHOW_ONLY_ALL_DIAG)
    result2 = execute_sql(SHOW_ONLY_ALL_SUBDIAG)
    return result, result2


# Get all separated diagnoses by part of code
def get_all_separated_diagnoses_by_part_of_code(part_of_code):
    return execute_sql(SHOW_ONLY_DIAG_BY_PART_CODE, [f'%{part_of_code}%']), \
        execute_sql(SHOW_ONLY_PODDIAG_BY_PART_CODE, [f'%{part_of_code}%'])


# Peel diagnoses to json
def peel_diagnoses(diags, subdiags):
    num_diags = 4

    result = {}

    for item in diags[0]:
        # Make code mkb in result
        code_mkb = item[num_diags]
        if code_mkb not in result:
            result[code_mkb] = {}

        # Make diagnose in result
        diag_name = item[num_diags + 1]
        if diag_name not in result[code_mkb]:
            result[code_mkb][diag_name] = {'omps': set(),
                                           'tactics': set(),
                                           'sub_diagnoses': {}}

        # Make omp in result
        omp = item[num_diags + 2]
        result[code_mkb][diag_name]['omps'].add(omp)

        # Make tactic in result
        tactic = item[num_diags + 3]
        result[code_mkb][diag_name]['tactics'].add(tactic)

        # Make recommendation in result
        tactic = item[num_diags + 4]
        result[code_mkb][diag_name]['diagnose_recommendation'] = tactic

    for item in subdiags[0]:
        code_mkb = item[num_diags]
        diagnose = item[num_diags + 1]
        sub_diagnose = item[num_diags + 2]

        # Make sub diagnose
        if sub_diagnose not in result[code_mkb][diagnose]['sub_diagnoses']:
            result[code_mkb][diagnose]['sub_diagnoses'][sub_diagnose] = {
                    'sub_diag_omps': set()
                }

        # Make omp to sub diagnose
        result[code_mkb][diagnose]['sub_diagnoses'][sub_diagnose][
            'sub_diag_omps'].add(item[num_diags + 3])

        # Make recommendation to sub diagnose
        result[code_mkb][diagnose]['sub_diagnoses'][sub_diagnose][
            'sub_diag_recommendation'] = item[num_diags + 4]

    return result


# Make cache full diagnoses or part if part code exitsts
def cache_diagnoses():
    result = peel_diagnoses(get_all_separated_diagnoses())
    cache.set('diagnoses_all', result, None)

    return result


def part_code(diags, subdiags):
    return peel_diagnoses(diags, subdiags)
