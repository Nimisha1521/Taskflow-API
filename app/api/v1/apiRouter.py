from fastapi import APIRouter 
from app.modules.tasks.router import router as task_router 
from app.modules.users.router import router as auth_router

api_router = APIRouter()
api_router.include_router(task_router)
api_router.include_router(auth_router)