from app.models.paises import Paises
from app.models.estados import Estados

from fastapi import FastAPI

app = FastAPI()
paises = Paises()
estados = Estados()

@app.get('/paises')
async def get_paises():
    return paises.get_all()

@app.get('/paises/nomes')
async def get_paises_nomes():
    return paises.get_names_only()

@app.get('/paises/{id}')
async def get_paises_id(id:int):
    return paises.get_by_id(id)

@app.get('/estados')
async def get_estados():
    return estados.get_all()

@app.get('/estados/nomes')
async def geta_estados_name_only():
    return estados.get_names_only()

@app.get('/estados/{id}')
async def get_estados_by_id(id:int):
    return estados.get_by_id(id)
