import os
import pyodbc
from app.config import settings
from pathlib import Path

os.environ["NLS_LANG"] = "BRAZILIAN PORTUGUESE_BRAZIL.WE8MSWIN1252"
os.environ["NLS_NUMERIC_CHARACTERS"] = ",."

BASE_DIR = Path(__file__).resolve().parent
INSTANT_CLIENT_PATH = str(BASE_DIR / "oracle" / "instantclient_21_21")
os.environ["PATH"] = INSTANT_CLIENT_PATH + os.path.pathsep + os.environ["PATH"]

conn_string = (
        f"DRIVER={settings.ORACLE_DRIVER};"
        f"DBQ={settings.ORACLE_HOST}:{settings.ORACLE_PORT}/{settings.ORACLE_SERVICE_NAME};"
        f"UID={settings.ORACLE_USERNAME};"
        f"PWD={settings.ORACLE_PASSWORD};"
    )

def get_db():
    print(conn_string, flush=True)
    conn = pyodbc.connect(conn_string)
    try:
        yield conn
    finally:
        conn.close()
