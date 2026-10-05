import pyodbc
import datetime
from app.repos.comparacao_safras import sql_comparacao_safras

async def get_comp_safras_data(conn: pyodbc.Connection):
    sqlres = sql_comparacao_safras(conn)
    reslist = []

    def serialize_date(val):
        if isinstance(val, (datetime.datetime, datetime.date)):
            return str(val.strftime("%d/%m/%Y"))
        return val

    for item in sqlres:
        resdict = {
            "grupo": item.get("GRUPO"),
            "var_in_codigo": item.get("VAR_IN_CODIGO"),
            "variavel": item.get("VARIAVEL"),
            "unidade": item.get("UNIDADE"),
            "dt_safra_anterior": serialize_date(item.get("DT_SAFRA_ANTERIOR")),
            "dt_safra_atual": serialize_date(item.get("DT_SAFRA_ATUAL")),
            "vl_dia_atual": item.get("VL_DIA_ATUAL"),
            "vl_safra_atual": item.get("VL_SAFRA_ATUAL"),
            "vl_safra_anterior": item.get("VL_SAFRA_ANTERIOR"),
            "dia_safra": item.get("DIA_SAFRA")
        }
        reslist.append(resdict)

    return reslist
