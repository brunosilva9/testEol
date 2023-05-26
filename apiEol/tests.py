from django.test import TestCase

# Create your tests here.

from django.db import connection

def execute_raw_sql(query): # for raw query
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    
if __name__ == "__main__":
    query = "SELECT * FROM events LIMIT 10"
    results = execute_raw_sql(query)
    for row in results:
        # Acceder a los valores de cada fila
        print(row)
