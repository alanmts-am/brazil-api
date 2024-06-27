from fastapi import APIRouter
from app.service.municipio_service import MunicipioService
from app.models.response import Response


municipio_router = APIRouter()
response = Response()
municipio_service = MunicipioService(response)


@municipio_router.get('/')
async def get_all_municipios():
    return municipio_service.get_all()


@municipio_router.get('/nomes')
async def get_municipios_name_only():
    return municipio_service.get_names_only()


@municipio_router.get('/{id}')
async def get_municipio_by_id(id: int):
    return municipio_service.get_by_id(id)
