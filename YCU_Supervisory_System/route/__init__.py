from fastapi import APIRouter

from YCU_Supervisory_System.route import division

api_router = APIRouter()
api_router.include_router()


