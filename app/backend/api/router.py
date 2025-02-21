from fastapi import APIRouter
from .basicInfoApi import router as basicInfo_router

api_router = APIRouter()
api_router.include_router(basicInfo_router, prefix="/basicInfo", tags=["basicInfo"])