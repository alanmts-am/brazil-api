from fastapi import APIRouter
from app.models.regioes import Regiao
from app.models.estados import Estado
from app.models.municipios import Municipio
from app.models.response import Response

regioes_router = APIRouter()
response = Response()

regioes = Regiao(response)
estados = Estado(response)
municipios = Municipio(response)


@regioes_router.get('/')
async def get_regioes():
    return regioes.get_all()


@regioes_router.get('/nomes')
async def get_regioes_name_only():
    return regioes.get_names_only()


@regioes_router.get('/{id}')
async def get_regioes_by_id(id: int):
    return regioes.get_by_id(id)


@regioes_router.get('/{id}/estados')
async def get_estados_from_regiao(id: int):
    return regioes.get_estados(estados.get_all()['estados'], id)


@regioes_router.get('/{id_regiao}/estados/{id_estado}')
async def get_estado_from_regiao(id_regiao: int, id_estado: int):
    return regioes.get_estado(estados.get_all()['estados'], id_regiao, id_estado)


@regioes_router.get('/{id_regiao}/estados/{id_estado}/municipios')
async def get_municipios_from_estado(id_regiao: int, id_estado: int):
    return regioes.get_municipios(municipios.get_all()['municipios'], id_regiao, id_estado)


@regioes_router.get('/{id_regiao}/estados/{id_estado}/municipios/{id_municipio}')
async def get_municipio_from_estado(id_regiao: int, id_estado: int, id_municipio: int):
    return regioes.get_municipio(municipios.get_all()['municipios'], id_regiao, id_estado, id_municipio)
