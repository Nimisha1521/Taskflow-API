from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy import Select
from sqlalchemy.orm import Session
from .schemas import TaskCreate, TaskPatch, TaskUpdate, TaskResponse
from .database import Base, engine, get_db
from .models import Task

Base.metadata.create_all(bind=engine)

app = FastAPI(title='TaskFlow API')

#The introductory API
@app.get("/")
def home():
   return {'message': 'TaskFlow API is running'}


#API to retrieve all the tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):

   statement = Select(Task).order_by(Task.id)
   return db.scalars(statement).all()


#API to filter tasks and display based on the completed attribute
@app.get("/tasks/filter")
#Define specific routes first and dynamic routes afterward.
def filter_tasks(completed: bool, db: Session = Depends(get_db)):

   statement = select(Task).where(Task.completed == completed)
   result = db.scalars(statement).all()
   return result

#API to retrive task based on task id 
#The {task_id} portion is a path parameter. If the request is GET /tasks/2, FastAPI extracts 2, converts it to an integer, and passes it to the function.If the value cannot be converted to an integer, FastAPI normally returns a 422 Unprocessable Entity validation response.
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
   task = db.get(Task, task_id)
   if task is None: 
      raise HTTPException(status_code=404, detail='Task not found')
   
   return task


#API for creating new task
@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate, db: Session = Depends(get_db)):
   try: 
      task = Task(**data.model_dump())
      db.add(task)
      db.commit()
      db.refresh(task)
      return task
   
   except Exception: 
      db.rollback()
      raise


#API for updating the task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def replace_task(task_id: int, data: TaskUpdate, db: Session= Depends(get_db)):
   task = db.get(Task, task_id)

   if task is None: 
      raise HTTPException(status_code=404, detail='Task Not Found')
   
   task.title = data.title
   task.completed = data.completed

   try: 
      db.commit()
      db.refresh(task)
      return task
   
   except Exception: 
      db.rollback()
      raise


#API for partial updates
@app.patch("/tasks/{task_id}", response_model=TaskResponse)
def patch_task(task_id: int, data: TaskPatch, db: Session = Depends(get_db)):
   task = db.get(Task, task_id)

   if task is None: 
      raise HTTPException(status_code=404, detail='No Task is found')
   
   changes = data.model_dump(exclude_unset=True)

   if any(value is None for value in changes.values()): 
      raise HTTPException(status_code=422, detail='Updated fields cannot be null')
   
   for field, value in changes.items():
      setattr(task, field, value)

   try: 
      db.commit()
      db.refresh(task)
      return task
   except Exception:
      db.rollback()
      raise


#API for deleting a task 
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
   task = db.get(Task, task_id)

   if task is None: 
      raise HTTPException(status_code=404, detail='Task not found')
 
   try:
      db.delete(task)
      db.commit()
      return task
   except Exception: 
      db.rollback()
      raise 
         