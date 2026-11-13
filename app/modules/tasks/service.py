from sqlalchemy.orm import Session
from app.modules.tasks import repository
from app.modules.tasks.models import Task
from app.modules.tasks.schemas import ( TaskCreate, TaskPatch, TaskUpdate)

def create_task(db: Session, data: TaskCreate) -> Task:
    return repository.create_task(db, data)

def get_all_tasks(db: Session) -> list[Task]:
    return repository.get_all_tasks(db)

def get_task_by_id(db: Session, task_id: int) -> Task | None:
    return repository.get_task_by_id(db, task_id)

def get_task_by_status(db: Session, completed: bool) -> list[Task]:
    return repository.get_task_by_status(db, completed)

def update_task(db: Session, task_id: int, data: TaskUpdate) -> Task | None:
    task = repository.get_task_by_id(db, task_id)
    if task is None:
        return None
    return repository.update_task(db, task, data)

def patch_task(db: Session, task_id: int, data: TaskPatch) -> Task | None:
    task = repository.get_task_by_id(db, task_id)
    if task is None:
        return None
    changes = data.model_dump(exclude_unset=True)
    if any(value is None for value in changes.values()):
        return ValueError('Updated Fields cannot be null')
    return repository.patch_task(db, task, changes)

def delete_task(db: Session, task_id: int) -> Task | None:
    task = repository.get_task_by_id(db, task_id)
    if task is None:
        return False
    repository.delete_task(db, task)
    return True