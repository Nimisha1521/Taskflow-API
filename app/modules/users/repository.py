from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.modules.users.models import User

class UserRepository:

    def __init__(self, db:Session):
        self.db = db

    def get_by_email(self, email:str):
        statement = select(User).where(email == User.email)
        return self.db.scalar(statement)

    def get_by_id(self, user_id: int):
        return self.db.get(User, user_id)

    def create(self, user: User):
        try:
            self.db.add(user)      #Adds the object to the session
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError:
            self.db.rollback()
            raise