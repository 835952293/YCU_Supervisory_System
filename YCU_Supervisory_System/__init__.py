from fastapi import APIRouter, FastAPI
from routers import api_router

app = FastAPI(
    title='宜春学院管理系统',
    description='......'
)

router = APIRouter()

@app.on_event('startup')
async def startup_event():
    setting.SERVICE_NAME = SERVICE_NAME
    app.include_router(api_router, prefix='/v1/api')
    app.include_router(api_router,prefix='/Super_system/v1/api')
    