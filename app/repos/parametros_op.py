import pyodbc

def sql_parametros_op(conn: pyodbc.Connection):
    query = """
        ...
    """

    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        
        results_dict = []
        for row in rows:
            item = {}
            for col_name, value in zip(columns, row):
                
                if isinstance(value, (float, int)) or type(value).__name__ == 'Decimal':
                    item[col_name] = str(value).replace('.', ',')
                else:
                    item[col_name] = value
            results_dict.append(item)

        print(results_dict)
        return results_dict
    finally:
        cursor.close()