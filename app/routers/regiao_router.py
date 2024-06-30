from fastapi import APIRouter
from app.models.regiao import Regiao
from app.models.estado import Estado
from app.models.municipio import Municipio
from app.service.regiao_service import RegiaoService
from app.service.estado_service import EstadoService
from app.service.municipio_service import MunicipioService
from typing import List

regiao_router = APIRouter()
regiao_service = RegiaoService()

estado_service = EstadoService()
municipios = MunicipioService()


@regiao_router.get('/', response_model=List[Regiao])
async def get_regioes():
    return regiao_service.get_all()


@regiao_router.get('/nomes', response_model=List[str])
async def get_regioes_name_only():
    return regiao_service.get_names_only()


@regiao_router.get('/{id}', response_model=Regiao)
async def get_regioes_by_id(id: int):
    return regiao_service.get_by_id(id)


@regiao_router.get('/{id}/estados', response_model=List[Estado])
async def get_estados_from_regiao(id: int):
    return regiao_service.get_estados(estado_service.get_data(), id)


@regiao_router.get('/{id_regiao}/estados/{id_estado}', response_model=Estado)
async def get_estado_from_regiao(id_regiao: int, id_estado: int):
    return regiao_service.get_estado(estado_service.get_data(), id_regiao, id_estado)


@regiao_router.get('/{id_regiao}/estados/{id_estado}/municipios', response_model=List[Municipio])
async def get_municipios_from_estado(id_regiao: int, id_estado: int):
    return regiao_service.get_municipios(municipios.get_data(), id_regiao, id_estado)


@regiao_router.get('/{id_regiao}/estados/{id_estado}/municipios/{id_municipio}', response_model=Municipio)
async def get_municipio_from_estado(id_regiao: int, id_estado: int, id_municipio: int):
    return regiao_service.get_municipio(municipios.get_data(), id_regiao, id_estado, id_municipio)
