import json

from datetime import date

from types import NoneType

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


# Execute custom sql-query with dictionary parameters
def execute_sql_dict(query: str, params={}):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        try:
            return cursor.fetchall(), cursor.description
        except Exception:
            return 'Success'


# Function to peel output from sql and return json like format
# Or if out is True then print it pretify in console
def peeler(data, out=False):
    description = [item.name for item in data[1]]

    result = []

    for item in data[0]:
        parsed = []

        for item2 in item:
            if type(item2) is str or type(item2) is int:
                parsed.append(item2)
            elif type(item2) is date:
                parsed.append(item2.strftime('%Y-%m-%d'))
            elif type(item2) is NoneType:
                parsed.append(None)
            else:
                print('Unknown type:', type(item2), 'with value:', item2)
                parsed.append('Unknown type')

        result.append(
            dict(
                zip(
                    description,
                    parsed
                )
            )
        )

    if out is True:
        print(json.dumps(result, indent=4))

    return result
