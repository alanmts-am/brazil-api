from fastapi import APIRouter
from app.models.estados import Estado
from app.models.municipios import Municipio


estados_router = APIRouter()
estados = Estado()
municipios = Municipio()


@estados_router.get('/')
async def get_estados():
    return estados.get_all()


@estados_router.get('/nomes')
async def geta_estados_name_only():
    return estados.get_names_only()


@estados_router.get('/{id}')
async def get_estados_by_id(id: int):
    return estados.get_by_id(id)


@estados_router.get('/{id}/municipios')
async def get_municipios_by_estado(id: int):
    return estados.get_municipios_from_estado(municipios.get_all(), id)
