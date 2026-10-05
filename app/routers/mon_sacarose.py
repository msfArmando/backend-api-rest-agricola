from typing import List
from app.schemas.mon_sacarose import MonSacaroseResponse, CompSafras, ParametrosOP
from app.services.mon_sacarose import get_mon_sacarose_data
from app.services.comparacao_safras import get_comp_safras_data
from app.services.parametros_op import get_parametros_op_data
import pyodbc
from fastapi import Depends, APIRouter, HTTPException
from app.database import get_db

router = APIRouter()

@router.get("/mon_sacarose", response_model=List[MonSacaroseResponse])
async def get_mon_sacarose(conn: pyodbc.Connection = Depends(get_db)):
    try:
        data = await get_mon_sacarose_data(conn)
        return data
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"API ERROR: {str(e)}"
        )
    
@router.get("/get_comp_safras", response_model=List[CompSafras])
async def get_comp_safras(conn: pyodbc.Connection = Depends(get_db)):
    try:
        data = await get_comp_safras_data(conn)
        return data
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"API ERROR: {str(e)}"
        )

@router.get("/get_parametros_op", response_model=List[ParametrosOP])
async def get_parametros_op(conn: pyodbc.Connection = Depends(get_db)):
    try:
        data = await get_parametros_op_data(conn)
        return data
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"API ERROR: {str(e)}"
        )