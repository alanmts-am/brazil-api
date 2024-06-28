from fastapi import APIRouter
from app.service.municipio_service import MunicipioService


municipio_router = APIRouter()
municipio_service = MunicipioService()


@municipio_router.get('/')
async def get_all_municipios():
    return municipio_service.get_all()


@municipio_router.get('/nomes')
async def get_municipios_name_only():
    return municipio_service.get_names_only()


@municipio_router.get('/{id}')
async def get_municipio_by_id(id: int):
    return municipio_service.get_by_id(id)
