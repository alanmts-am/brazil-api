from app.models.paises import Paises

from fastapi import FastAPI

app = FastAPI()
paises = Paises()

@app.get('/paises')
async def get_paises():
    return paises.getAll()

@app.get('/paises/{id}')
async def get_paises_id(id:int):
    return paises.getById(id)
