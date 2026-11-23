from sqlalchemy.orm import Session
from app.modules.users.models import User
from app.core.security import hash_password, verify_password
from app.modules.users.repository import UserRepository
from app.modules.users.schemas import UserCreate
from sqlalchemy.exc import IntegrityError

class UserService:
    def __init__(self,db: Session):
        self.repository = UserRepository(db)

    def registerUser(self, userData: UserCreate) -> User:
        existing_user = self.repository.get_by_email(userData.email)
        if existing_user: 
            raise ValueError("Email is already registered.")
        hashed_password = hash_password(userData.password)
        new_user = User(name = userData.name, email = userData.email, hashed_password = hashed_password)

        try:
            return self.repository.create(new_user)
        except IntegrityError:
            raise ValueError("Email is already registered.")

        #Integrity constant exception and race condition 
        #The service-level email check gives a quick, readable error in ordinary cases; the database unique constraint handles concurrent requests reliably. Catching and translating the database exception makes the API robust.

    def authenticate_user(self, email: str, password: str) -> User:
        user = self.repository.get_by_email(email)

        if not user: 
            raise ValueError("Incorrect email or password.")
        
        if not verify_password(password, user.hashed_password):
            raise ValueError("Incorrect email or password.")

        if not user.is_active:
            raise ValueError("Your account is inactive.")

        return user

#JWT uses the exp claim, represented as a Unix timestamp.