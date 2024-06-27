from fastapi import APIRouter
from app.service.estado_service import EstadoService
from app.models.response import Response


estado_router = APIRouter()
response = Response()
estado_service = EstadoService(response)


@estado_router.get('/')
async def get_estados():
    return estado_service.get_all()


@estado_router.get('/nomes')
async def geta_estados_name_only():
    return estado_service.get_names_only()


@estado_router.get('/{id}')
async def get_estados_by_id(id: int):
    return estado_service.get_by_id(id)
