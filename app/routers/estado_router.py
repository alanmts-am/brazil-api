from fastapi import APIRouter
from app.models.estado import Estado
from app.service.estado_service import EstadoService
from typing import List


estado_router = APIRouter()
estado_service = EstadoService()


@ estado_router.get('/', response_model=List[Estado])
async def get_estados():
    return estado_service.get_all()


@ estado_router.get('/nomes', response_model=List[str])
async def geta_estados_name_only():
    return estado_service.get_names_only()


@ estado_router.get('/{id}', response_model=Estado)
async def get_estados_by_id(id: int):
    return estado_service.get_by_id(id)
