import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DB_URL = os.environ['SQLALCHEMY_DB_URL']
engine = create_engine(
    SQLALCHEMY_DB_URL,
    pool_pre_ping= True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
