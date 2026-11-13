from pydantic import BaseModel, ConfigDict, Field
#BaseModel defines the data structure and enables validation.
#ConfigDict changes the rules governing how a model handles data.
#Field defines additional rules for individual fields.

class TaskCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    title: str = Field(min_length=1, max_length=120)
    completed: bool = False

class TaskUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    title: str = Field(min_length=1, max_length=120)
    completed: bool 

class TaskPatch(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    title: str | None = Field(default=None, min_length=1, max_length=120)
    completed: bool | None = None

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True) #Previously, our endpoints returned dictionaries. Now, SQLAlchemy will return Task objects. With from_attributes=True, Pydantic can read attributes such as task.id and task.title to construct the response model.This setting allows Pydantic to read values from ORM object attributes.
    id: int
    title: str
    completed: bool