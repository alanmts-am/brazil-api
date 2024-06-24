from fastapi import APIRouter
from app.models.paises import Pais


paises_router = APIRouter()
paises = Pais()


@paises_router.get('/')
async def get_paises():
    return paises.get_all()


@paises_router.get('/nomes')
async def get_paises_nomes():
    return paises.get_names_only()


@paises_router.get('/{id}')
async def get_paises_id(id: int):
    return paises.get_by_id(id)
