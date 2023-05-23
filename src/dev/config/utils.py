from django.db import connection


# Function for db-executor
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


# Execute custom sql-query with parameters
def execute_sql(query: str, params=[]):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        return cursor.fetchall(), cursor.description
