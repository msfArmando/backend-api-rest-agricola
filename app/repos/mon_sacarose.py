import pyodbc

def sql_mon_sacarose(conn: pyodbc.Connection, data_ini: str, data_end: str):
    query = """
        ...
    """

    cursor = conn.cursor()

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        results_dict = [dict(zip(columns, row)) for row in rows]
        return results_dict
    finally:
        cursor.close()

    
