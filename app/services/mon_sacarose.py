import pyodbc
from datetime import datetime
from app.repos.mon_sacarose import sql_mon_sacarose

async def get_mon_sacarose_data(conn: pyodbc.Connection):

    today_date = datetime.now()
    today_format = today_date.strftime("%d-%m-%Y")
    sqlres = sql_mon_sacarose(conn, today_format, today_format)

    reslist: list[dict] = []

    for item in sqlres:
        resdict = {
            "equipamento": item.get("EQUIPAMENTOS"),
            "unidade": item.get("UNIDADE"),
            "safra": item.get("SAFRA"),
            "cod_variavel": item.get("COD_VARIAVEL"),
            "parametros": item.get("PARAMETROS"),
            "turno_a": str(item.get("TURNO_A")) if item.get("TURNO_A") else '-',
            "turno_b": str(item.get("TURNO_B")) if item.get("TURNO_B") else '-',
            "turno_c": str(item.get("TURNO_C")) if item.get("TURNO_C") else '-',
            "media_dia": str(item.get("MEDIA_DIA")) if item.get("MEDIA_DIA") else '-'
        }
        reslist.append(resdict)

    return reslist