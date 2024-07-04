import os
from app.routers.base_router import base_router
from app.routers.country_router import country_router
from app.routers.state_router import state_router
from app.routers.region_router import region_router
from app.routers.city_router import city_router

from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
API_BASE_PATH = os.getenv("API_BASE_PATH")
API_VERSION = os.getenv("API_VERSION")

app = FastAPI(title="BRAZIL API",
              description="This a BRAZIL api service to get data from countries, states, regions and cities",
              version=API_VERSION)

app.include_router(base_router)
app.include_router(base_router, prefix=API_BASE_PATH)
app.include_router(
    country_router, prefix=f'{API_BASE_PATH}/countries', tags=['countries'])
app.include_router(
    state_router, prefix=f'{API_BASE_PATH}/states', tags=['states'])
app.include_router(
    region_router, prefix=f'{API_BASE_PATH}/regions', tags=['regions'])
app.include_router(
    city_router, prefix=f'{API_BASE_PATH}/cities', tags=['cities'])
