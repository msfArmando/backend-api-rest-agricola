from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import mon_sacarose

app = FastAPI(
    title = "API GOD",
    description = "API Agrícola do Grupo Olho D'Água",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mon_sacarose.router, prefix="/api", tags=["mon_sacarose"])