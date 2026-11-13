#The repository does not need to know whether the request came from Swagger, a mobile application or another service.
#It only needs to perform the requested data operation.

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.modules.tasks.schemas import TaskCreate, TaskUpdate, TaskPatch
from app.modules.tasks.models import Task

def create_task(db: Session, data: TaskCreate) -> Task:
    task = Task(**data.model_dump())
    try: 
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    except Exception: 
        db.rollback()
        raise 

def get_all_tasks(db: Session) -> list[Task]:
    statement = select(Task).order_by(Task.id)
    return db.scalars(statement).all()
    
def get_task_by_id(db: Session, task_id: int) -> Task | None:
    return db.get(Task, task_id)

def get_task_by_status(db: Session, completed: bool) -> list[Task]:
    statement = select(Task).where(Task.completed == completed)
    return db.scalars(statement).all()

def update_task(db: Session, task: Task, data: TaskUpdate) -> Task | None:
    task.title = data.title
    task.completed = data.completed 
    try:
        db.commit()
        db.refresh(task)
        return task
    except Exception:
        db.rollback()
        raise
        
def patch_task(db: Session, task: Task, changes: dict) -> Task | None:
    for field, value in changes.items():
        setattr(Task, field, value)
    try: 
        db.commit()
        db.refresh(task)
        return task
    except Exception: 
        db.rollback()
        raise


def delete_task(db: Session, task_id: int) -> Task | None:
    task = db.get(Task, task_id)
    try:
        db.delete(task)
        db.commit()
        return task
    except Exception: 
        db.rollback()
        raise