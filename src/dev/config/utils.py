from django.db import connection


def execute(query: str, params: str):
    with connection.cursor() as cursor:
        try:
            if params != ['']:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return True, cursor.fetchall(), \
                [descr[0] for descr in cursor.description]
        except Exception as e:
            print(e)
            return False, str(e)
