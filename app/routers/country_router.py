from fastapi import APIRouter, HTTPException
from app.service.country_service import CountryService
from app.models.country import Country
from typing import List

country_router = APIRouter()
country_service = CountryService()


@country_router.get('/', response_model=List[Country])
async def get_countries():
    return country_service.get_all()


@ country_router.get('/names', response_model=List[str])
async def get_countries_names():
    return country_service.get_names_only()


@ country_router.get('/{id}', response_model=Country)
async def get_countries_id(id: int):
    country = country_service.get_by_id(id)
    if country == []:
        raise HTTPException(status_code=404, detail="Country not found")
    elif country == None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return country
