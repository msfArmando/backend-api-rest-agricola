import pyodbc
import datetime
from app.repos.parametros_op import sql_parametros_op


async def get_parametros_op_data(conn: pyodbc.Connection):
    sqlres = sql_parametros_op(conn)
    reslist = []

    for item in sqlres:

        cod_var = item.get("COD_VARIAVEL")
        cod_var_float = 0.0
        cod_var_int = 0
        cod_var_str = ""

        if cod_var:
            cod_var_new = cod_var.replace(',', '.')
            cod_var_float = float(cod_var_new)
            cod_var_int = int(cod_var_float)
            cod_var_str = str(cod_var_int)
        else:
            cod_var_str = "-"

        print(item.get("dezessete"))

        resdict = {
            "fil_in_codigo": item.get("FIL_IN_CODIGO"),
            "grupo": item.get("GRUPO"),
            "variavel": item.get("VARIAVEL"),
            "unidade": item.get("UNIDADE"),
            "safra": item.get("SAFRA"),
            "cod_variavel": cod_var_str,
            "vlr_min": str(item.get("VLR_MIN")) if item.get("VLR_MIN") else "-",
            "vlr_max": str(item.get("VLR_MAX")) if item.get("VLR_MAX") else "-",
            "nove": str(item.get("nove")) if item.get("nove") else "-",
            "treze": str(item.get("treze")) if item.get("treze") else "-",
            "dezessete": str(item.get("dezessete")) if item.get("dezessete") else "-",
            "vinteeum": str(item.get("vinteeum")) if item.get("vinteeum") else "-",
            "um": str(item.get("um")) if item.get("um") else "-",
            "cinco": str(item.get("cinco")) if item.get("cinco") else "-",
            "media_dia": str(item.get("MEDIA_DIA")) if item.get("MEDIA_DIA") else "-"
        }
        reslist.append(resdict)

    return reslist
