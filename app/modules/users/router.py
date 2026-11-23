from fastapi import APIRouter, Depends, HTTPException, status  #APIRouter allows us to organize related endpoints separately from main.py.Instead of placing every endpoint inside one large file, we create feature-specific routers.
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.users.schemas import UserCreate, UserResponse, LoginRequest
from app.modules.users.service import UserService
from app.core.security import create_access_token
from app.modules.users.schemas import Token

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

@router.post("/login", response_model=Token, status_code= status.HTTP_200_OK)
def login_user(user_data: LoginRequest, db: Session = Depends(get_db)):
    user_service = UserService(db)
    try: 
        user = user_service.authenticate_user(user_data.email, user_data.password)
        access_token = create_access_token(data= {'sub': str(user.id)})
        return {"access_token" : access_token, "token_type": 'bearer'}
    except ValueError as error: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(error), headers={"WWW-Authenticate": "Bearer"}) from error
    #headers={"WWW-Authenticate": "Bearer"} Tells the client that the API uses Bearer Token authentication. This is commonly used with JWT access tokens.
    # from error - Uses Python's exception chaining to preserve the original exception as the cause of the new HTTPException.This helps developers trace the original error during debugging.