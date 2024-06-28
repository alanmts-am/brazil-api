from fastapi import APIRouter
from app.service.pais_service import PaisService
from app.models.pais import Pais
from typing import List, Dict

paises_router = APIRouter()
pais_service = PaisService()


@ paises_router.get('/', response_model=List[Pais])
async def get_paises():
    return pais_service.get_all()


@ paises_router.get('/nomes', response_model=List[str])
async def get_paises_nomes():
    return pais_service.get_names_only()


@ paises_router.get('/{id}')
async def get_paises_id(id: int):
    return pais_service.get_by_id(id)
