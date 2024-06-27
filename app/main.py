from app.routers.pais_router import paises_router
from app.routers.estado_router import estado_router
from app.routers.regiao_router import regiao_router
from app.routers.municipio_router import municipio_router

from fastapi import FastAPI

app = FastAPI()
app.mount(path="/api", app=app)

app.include_router(paises_router, prefix='/paises', tags=['paises'])
app.include_router(estado_router, prefix='/estados', tags=['estados'])
app.include_router(regiao_router, prefix='/regioes', tags=['regioes'])
app.include_router(municipio_router, prefix='/municipios',
                   tags=['municipios'])
