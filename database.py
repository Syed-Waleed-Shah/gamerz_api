import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///data.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=True, autoflush=True, expire_on_commit=True, bind=engine)

Base = declarative_base()


# Dependency
def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()