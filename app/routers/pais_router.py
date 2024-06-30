from fastapi import APIRouter, HTTPException
from app.service.pais_service import PaisService
from app.models.pais import Pais
from typing import List

paises_router = APIRouter()
pais_service = PaisService()


@paises_router.get('/', response_model=List[Pais])
async def get_paises():
    return pais_service.get_all()


@ paises_router.get('/nomes', response_model=List[str])
async def get_paises_nomes():
    return pais_service.get_names_only()


@ paises_router.get('/{id}', response_model=Pais)
async def get_paises_id(id: int):
    pais = pais_service.get_by_id(id)
    if pais == []:
        raise HTTPException(status_code=404, detail="Pais not found")
    elif pais == None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return
