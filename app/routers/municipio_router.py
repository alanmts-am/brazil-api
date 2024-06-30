from fastapi import APIRouter
from app.models.municipio import Municipio
from app.service.municipio_service import MunicipioService
from typing import List


municipio_router = APIRouter()
municipio_service = MunicipioService()


@municipio_router.get('/', response_model=List[Municipio])
async def get_all_municipios():
    return municipio_service.get_all()


@municipio_router.get('/nomes', response_model=List[str])
async def get_municipios_name_only():
    return municipio_service.get_names_only()


@municipio_router.get('/{id}', response_model=Municipio)
async def get_municipio_by_id(id: int):
    return municipio_service.get_by_id(id)
