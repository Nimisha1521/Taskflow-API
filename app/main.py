from fastapi import FastAPI, HTTPException, status
from schemas import TaskCreate, TaskPatch, TaskUpdate, TaskResponse

#Stage 1: Using in memory storage

app = FastAPI(title='TaskFlow API')

tasks: list[dict] = [
   {'id': 1, 'title': 'Learn Python', 'completed': False},
   {'id': 2, 'title': 'Learn FastApi', 'completed': False},
]

@app.get("/")
def home():
   return {'message': 'TaskFlow API is running'}

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
   return tasks

@app.get("/tasks/filter")
#Define specific routes first and dynamic routes afterward.
def filter_tasks(completed: bool):
   result=[]
   for task in tasks: 
      if task['completed'] == completed: 
        result.append(task)
   return result  

#The {task_id} portion is a path parameter. If the request is GET /tasks/2, FastAPI extracts 2, converts it to an integer, and passes it to the function.If the value cannot be converted to an integer, FastAPI normally returns a 422 Unprocessable Entity validation response.
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
   for task in tasks: 
      if task['id'] == task_id:
        return task
   raise HTTPException(status_code=404, detail='Task Not Found')
  

@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate):
   new_id = max((task['id'] for task in tasks), default=0) + 1
   new_task = {
      "id": new_id,
      **data.model_dump()
   }
   tasks.append(new_task)
   #json converted into a Pydantic model instance that you can access using data.
   return new_task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def replace_task(task_id: int, data: TaskUpdate):
   for index, task in enumerate(tasks):
      if task["id"] == task_id:
        updated_task = {
           "id" : task_id,
           **data.model_dump()
        }
        task[index] = updated_task
        return updated_task
   raise HTTPException(status_code=404, detail="Task not found")
   

@app.patch("/tasks/{task_id}", response_model=TaskResponse)
def patch_task(task_id: int, data: TaskPatch):
    for task in tasks:
        if task["id"] == task_id:
            changes = data.model_dump(exclude_unset=True)

            if any(value is None for value in changes.values()): raise HTTPException(status_code=422,detail="Updated fields cannot be null")

            task.update(changes)
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
   for index, task in enumerate(tasks):
      if task['id'] == task_id:
        deleted_task = tasks.pop(index)
        return {'message' : 'Task Deleted', 'task': deleted_task}
   raise HTTPException(status_code=404, detail='Task not found')
         