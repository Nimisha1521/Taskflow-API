from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.exceptions import TaskNotFoundError
from app.api.v1.apiRouter import api_router

app = FastAPI(title="TaskFlow API", description="Task management backend built using FastAPI and PostgreSQL", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")

@app.exception_handler(TaskNotFoundError)
async def task_not_found_handler(request = Request, exc = TaskNotFoundError):
   return JSONResponse(status_code=404, content={'detail': str(exc)})
   

#The introductory API
@app.get("/")
def home():
   return {'message': 'TaskFlow API is running'}
