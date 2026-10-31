from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import sqlite3

database_url = 'sqlite:///./taskflow.db'

engine = create_engine(
    database_url, 
    connect_args= {"check_same_thread" : False},
)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

def get_db():
    db = SessionLocal()
    #But Python has another concept: callable objects.A callable object is an object that you can execute using parentheses ().
    try: 
        yield db 
    finally:
        db.close()
