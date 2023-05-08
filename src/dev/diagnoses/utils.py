from django.db import connection

# from dbsetter.diagnoses.request import (
#     SHOW_DIAG_BY_CODE,
# )


def get_diagnose_by_field(field: str):
    with connection.cursor() as cursor:
        # cursor.execute(SHOW_DIAG_BY_CODE, [field,])
        cursor.execute('select * from account_user', [field,]) # Change it
        return cursor.fetchall()
