from fastapi import APIRouter
from app.models.region import Region
from app.models.state import State
from app.models.city import City
from app.service.region_service import RegionService
from app.service.state_service import StateService
from app.service.city_service import CityService
from typing import List

region_router = APIRouter()
region_service = RegionService()

state_service = StateService()
city_service = CityService()


@region_router.get('/', response_model=List[Region])
async def get_regions():
    return region_service.get_all()


@region_router.get('/names', response_model=List[str])
async def get_regions_name_only():
    return region_service.get_names_only()


@region_router.get('/{id}', response_model=Region)
async def get_regions_by_id(id: int):
    return region_service.get_by_id(id)


@region_router.get('/{id}/states', response_model=List[State])
async def get_states_from_region(id: int):
    return region_service.get_states(state_service.get_all(), id)


@region_router.get('/{id_regiao}/states/{id_estado}', response_model=State)
async def get_state_from_region(id_regiao: int, id_estado: int):
    return region_service.get_state(state_service.get_all(), id_regiao, id_estado)


@region_router.get('/{id_regiao}/states/{id_estado}/cities', response_model=List[City])
async def get_cities_from_state(id_regiao: int, id_estado: int):
    return region_service.get_cities(city_service.get_all(), id_regiao, id_estado)


@region_router.get('/{id_regiao}/states/{id_estado}/cities/{id_municipio}', response_model=City)
async def get_city_from_state(id_regiao: int, id_estado: int, id_municipio: int):
    return region_service.get_city(city_service.get_all(), id_regiao, id_estado, id_municipio)
