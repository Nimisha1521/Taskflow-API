from fastapi import FastAPI
from app.api.v1.apiRouter import api_router

app = FastAPI(title="TaskFlow API", description="Task management backend built using FastAPI and PostgreSQL", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")

#The introductory API
@app.get("/")
def home():
   return {'message': 'TaskFlow API is running'}
