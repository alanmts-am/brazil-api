from fastapi import APIRouter
from app.models.regioes import Regioes

regioes_router = APIRouter()
regioes = Regioes()


@regioes_router.get('/')
async def get_regioes():
    return regioes.get_all()


@regioes_router.get('/nomes')
async def get_regioes_name_only():
    return regioes.get_names_only()


@regioes_router.get('/{id}')
async def get_regioes_by_id(id: int):
    return regioes.get_by_id(id)
