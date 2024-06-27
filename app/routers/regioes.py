from fastapi import APIRouter
from app.service.regiao_service import RegiaoService
from app.service.estado_service import EstadoService
from app.service.municipio_service import MunicipioService
from app.models.response import Response

regiao_router = APIRouter()
response = Response()
regiao_service = RegiaoService(response)

estado_service = EstadoService(response)
municipios = MunicipioService(response)


@regiao_router.get('/')
async def get_regioes():
    return regiao_service.get_all()


@regiao_router.get('/nomes')
async def get_regioes_name_only():
    return regiao_service.get_names_only()


@regiao_router.get('/{id}')
async def get_regioes_by_id(id: int):
    return regiao_service.get_by_id(id)


@regiao_router.get('/{id}/estados')
async def get_estados_from_regiao(id: int):
    return regiao_service.get_estados(estado_service.get_data(), id)


@regiao_router.get('/{id_regiao}/estados/{id_estado}')
async def get_estado_from_regiao(id_regiao: int, id_estado: int):
    return regiao_service.get_estado(estado_service.get_data(), id_regiao, id_estado)


@regiao_router.get('/{id_regiao}/estados/{id_estado}/municipios')
async def get_municipios_from_estado(id_regiao: int, id_estado: int):
    return regiao_service.get_municipios(municipios.get_data(), id_regiao, id_estado)


@regiao_router.get('/{id_regiao}/estados/{id_estado}/municipios/{id_municipio}')
async def get_municipio_from_estado(id_regiao: int, id_estado: int, id_municipio: int):
    return regiao_service.get_municipio(municipios.get_data(), id_regiao, id_estado, id_municipio)
