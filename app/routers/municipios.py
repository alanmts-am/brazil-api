from fastapi import APIRouter
from app.models.municipios import Municipio


municipios_router = APIRouter()
municipios = Municipio()


@municipios_router.get('/')
async def get_all_municipios():
    return municipios.get_all()


@municipios_router.get('/nomes')
async def get_municipios_name_only():
    return municipios.get_names_only()


@municipios_router.get('/{id}')
async def get_municipio_by_id(id: int):
    return municipios.get_by_id(id)
