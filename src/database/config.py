from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database/todo.db")
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

def init_db():
    Base.metadata.create_all(engine)
    
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()