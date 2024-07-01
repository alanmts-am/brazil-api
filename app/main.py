import os
from app.routers.country_router import country_router
from app.routers.state_router import state_router
from app.routers.region_router import region_router
from app.routers.city_router import city_router

from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="BRAZIL API",
              description="This a BRAZIL api service to get data from countries, states, regions and cities",
              version=os.getenv("API_VERSION"))
app.mount(path=os.getenv("API_BASE_PATH"), app=app)

app.include_router(country_router, prefix='/countries', tags=['countries'])
app.include_router(state_router, prefix='/states', tags=['states'])
app.include_router(region_router, prefix='/regions', tags=['regions'])
app.include_router(city_router, prefix='/cities',
                   tags=['cities'])


@app.get("/")
async def root():
    return {"message": "Welcome!"}
