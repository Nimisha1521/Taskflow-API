from fastapi import APIRouter, Depends, HTTPException, status  #APIRouter allows us to organize related endpoints separately from main.py.Instead of placing every endpoint inside one large file, we create feature-specific routers.
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.users.schemas import UserCreate, UserResponse
from app.modules.users.service import UserService

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post("/register", response_model=UserResponse, status_code= status.HTTP_201_CREATED)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    #db: Session = Depends(get_db) This is dependency injection. FastAPI calls get_db(), obtains a database session and provides it to the endpoint. You do not need to manually create a database session inside this function.
    user_service = UserService(db)
    try:
        return user_service.registerUser(user_data)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error)) from error
    #response_model=UserResponse - FastAPI serializes the returned object according to the response schema. The password hash is therefore excluded from the API response.
    #from error is Python's exception chaining mechanism.