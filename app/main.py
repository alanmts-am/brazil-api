from app.models.paises import Paises

from fastapi import FastAPI

app = FastAPI()
paises = Paises()

@app.get('/paises')
async def get_municipios():
    return paises.getAll()

@app.get('/paises/{id}')
async def get_municipios(id:int):
    ps = paises.getAll()
    for p in ps:
        if p['id'] == id:
            return p
