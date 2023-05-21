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


# Parse query result to human readable view of data
def parse_data_to_client(query, trash_amount: int = 0):
    result: list = []
    data, descr = query

    # Peel description for zip function
    peeled_descr = []
    for item in descr:
        peeled_descr.append(item.name)

    # Merge data with description
    for item in data:
        result.append(
            dict(
                zip(
                    peeled_descr[trash_amount:],
                    item[trash_amount:]
                    )
                )
            )

    return result
