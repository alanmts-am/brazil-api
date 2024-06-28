import os
from app.routers.pais_router import paises_router
from app.routers.estado_router import estado_router
from app.routers.regiao_router import regiao_router
from app.routers.municipio_router import municipio_router

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()


async def http_not_found(request, exc):
    return JSONResponse(content={'status': exc.status_code, 'message': 'Not found'}, status_code=exc.status_code)

exception_handlers = {
    404: http_not_found
}

app = FastAPI(title="IBGE API",
              description="This a IBGE api service to get data from countries, states, regions and cities",
              version=os.getenv("API_VERSION"),
              exception_handlers=exception_handlers)
app.mount(path=os.getenv("API_BASE_PATH"), app=app)

app.include_router(paises_router, prefix='/paises', tags=['paises'])
app.include_router(estado_router, prefix='/estados', tags=['estados'])
app.include_router(regiao_router, prefix='/regioes', tags=['regioes'])
app.include_router(municipio_router, prefix='/municipios',
                   tags=['municipios'])


@app.get("/")
async def root():
    return {"message": "Welcome! This is a IBGE Api service"}
