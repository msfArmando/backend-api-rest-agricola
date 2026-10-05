import pyodbc

def sql_comparacao_safras(conn: pyodbc.Connection):
    query = """
        ...
    """

    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        results_dict = [dict(zip(columns, row)) for row in rows]
        print("RESULTADOS D A  C O N S U L T A  S Q L  !!", flush=True)
        print(results_dict, flush=True)
        return results_dict
    finally:
        cursor.close()