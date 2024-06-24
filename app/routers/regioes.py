from fastapi import APIRouter
from app.models.regioes import Regiao
from app.models.estados import Estado
from app.models.municipios import Municipio

regioes_router = APIRouter()
regioes = Regiao()
estados = Estado()
municipios = Municipio()


def get_estado(estados: list, id_regiao: int, id_estado: int):
    estados_regiao = regioes.get_estados_from_regiao(
        estados, id_regiao)

    for estado in estados_regiao:
        if estado['id'] == id_estado:
            return estado


def get_municipio(municipios: list, id_regiao: int, id_estado: int, id_municipio: int):
    municipios_estado = []

    for municipio in municipios:
        if municipio['id'] == id_municipio and municipio['estado']['id'] == id_estado and municipio['estado']['regiao']['id'] == id_regiao:
            municipios_estado.append(municipio)

    return municipios_estado


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
    return regioes.get_estados_from_regiao(estados.get_all(), id)


@regioes_router.get('/{id_regiao}/estados/{id_estado}')
async def get_estado_from_regiao(id_regiao: int, id_estado: int):
    return get_estado(estados.get_all(), id_regiao, id_estado)


@regioes_router.get('/{id_regiao}/estados/{id_estado}/municipios')
async def get_municipios_from_estado(id_regiao: int, id_estado: int):
    estado = get_estado(estados.get_all(), id_regiao, id_estado)

    return estados.get_municipios_from_estado(municipios.get_all(), estado['id'])


@regioes_router.get('/{id_regiao}/estados/{id_estado}/municipios/{id_municipio}')
async def get_municipio_from_estado(id_regiao: int, id_estado: int, id_municipio: int):
    return get_municipio(municipios.get_all(), id_regiao, id_estado, id_municipio)
