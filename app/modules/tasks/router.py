
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.tasks.models import Task
from app.modules.tasks.schemas import TaskCreate, TaskUpdate, TaskPatch, TaskResponse
from app.modules.tasks import service

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return service.get_all_tasks(db)

@router.get("/filter", response_model=list[TaskResponse])
def filter_tasks(completed: bool, db: Session = Depends(get_db)):
    return service.get_task_by_status(db, completed)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return service.get_task_by_id(db, task_id)


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate, db: Session = Depends(get_db)):
    return service.create_task(db, data)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task( task_id: int, data: TaskUpdate, db: Session = Depends(get_db)):
    return service.update_task(db, task_id, data)

@router.patch("/{task_id}", response_model=TaskResponse)
def patch_task( task_id: int, data: TaskPatch, db: Session = Depends(get_db)):
    return service.patch_task(db, task_id, data)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return service.delete_task(db, task_id)