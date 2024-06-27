from fastapi import APIRouter
from app.service.pais_service import PaisService
from app.models.response import Response

paises_router = APIRouter()
response = Response()
pais_service = PaisService(response)


@paises_router.get('/')
async def get_paises():
    return pais_service.get_all()


@paises_router.get('/nomes')
async def get_paises_nomes():
    return pais_service.get_names_only()


@paises_router.get('/{id}')
async def get_paises_id(id: int):
    return pais_service.get_by_id(id)
