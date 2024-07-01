from fastapi import APIRouter
from app.models.city import City
from app.service.city_service import CityService
from typing import List


city_router = APIRouter()
city_service = CityService()


@city_router.get('/', response_model=List[City])
async def get_all_cities():
    return city_service.get_all()


@city_router.get('/names', response_model=List[str])
async def get_cities_name_only():
    return city_service.get_names_only()


@city_router.get('/{id}', response_model=City)
async def get_city_by_id(id: int):
    return city_service.get_by_id(id)
