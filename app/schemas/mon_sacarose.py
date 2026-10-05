from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class MonSacaroseResponse(BaseModel):
    equipamento: str
    unidade: str
    safra: int
    cod_variavel: int
    parametros: str
    turno_a: str
    turno_b: str
    turno_c: str
    media_dia: str

class CompSafras(BaseModel):
    grupo: Optional[str] = None
    var_in_codigo: Optional[int] = None   
    variavel: Optional[str] = None       
    unidade: Optional[str] = None
    dt_safra_anterior: Optional[str] = None  
    dt_safra_atual: Optional[str] = None     
    vl_dia_atual: Optional[Decimal] = None
    vl_safra_atual: Optional[Decimal] = None
    vl_safra_anterior: Optional[Decimal] = None
    dia_safra: Optional[int] = None

class ParametrosOP(BaseModel):
    fil_in_codigo: str = None
    grupo: str = None
    variavel: str = None
    unidade: str = None
    safra: str = None
    cod_variavel: str = None
    vlr_min: str = None
    vlr_max: str = None
    nove: str = None
    treze: str = None
    dezessete: str = None
    vinteeum: str = None
    um: str = None
    cinco: str = None
    media_dia: str = None
    