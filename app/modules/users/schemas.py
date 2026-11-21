from pydantic import BaseModel, ConfigDict, Field, EmailStr

class UserCreate(BaseModel):  #Base Model provide data validation and parsing 
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password : str = Field(min_length=8, max_length=128)

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr    #Check the correctness of the email synatax and install dependency pip install email-validator
    is_active: bool 
    model_config = ConfigDict(from_attributes=True)    # It tells Pydantic to read the object's properties using dot notation (obj.username) instead.

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)