from fastapi import APIRouter
from app.models.estados import Estados


estados_router = APIRouter()
estados = Estados()


@estados_router.get('/')
async def get_estados():
    return estados.get_all()


@estados_router.get('/nomes')
async def geta_estados_name_only():
    return estados.get_names_only()


@estados_router.get('/{id}')
async def get_estados_by_id(id: int):
    return estados.get_by_id(id)
