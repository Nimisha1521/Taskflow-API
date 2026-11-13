from fastapi import FastAPI, Request, logger
from fastapi.responses import JSONResponse
from app.core.exceptions import TaskNotFoundError
from app.api.v1.apiRouter import api_router
import time

app = FastAPI(title="TaskFlow API", description="Task management backend built using FastAPI and PostgreSQL", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")

@app.exception_handler(TaskNotFoundError)
async def task_not_found_handler(request = Request, exc = TaskNotFoundError):
   return JSONResponse(status_code=404, content={'detail': str(exc)})

@app.middleware("http")
async def log_requests(request: Request, call_next):
   start_time = time.perf_counter()
   logger.info("Incomming request: %s %s", request.method, request.url.path)

   response = await call_next(request)
   process_time = time.perf_counter() - start_time

   logger.info("Completed request: %s %s | Status: %s | Time: %.4fs", request.method, request.url.path, response.status_code, process_time)
   return response

#The introductory API
@app.get("/")
def home():
   return {'message': 'TaskFlow API is running'}
