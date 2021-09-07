from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from fastapi_todo.db import Base


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    f_name = Column(String)
    l_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    todos = relationship("TodoModel", back_populates="owner", cascade="all, delete-orphan")
