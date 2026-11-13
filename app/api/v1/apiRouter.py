from fastapi import APIRouter 
from app.modules.tasks.router import router as task_router 

api_router = APIRouter()
api_router.include_router(task_router)