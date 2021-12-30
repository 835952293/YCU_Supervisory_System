from fastapi import APIRouter

from YCU_Supervisory_System.routers import division

api_router = APIRouter()
api_router.include_router()