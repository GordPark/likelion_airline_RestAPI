from pydantic import BaseModel

# user_table
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserTable(Base):
    __tablename__ = 'users'
    __table_args__ = {"schema": "public"}  # public 스키마 사용
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)


# model
class UserModel(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str

class UserCreate(UserModel):
    firstName: str
    lastName: str
    email: str
    password: str

class UserUpdate(UserModel):
    irstName: str = None
    lastName: str = None
    email: str = None
    password: str = None

class User(UserModel):
    id: int

    class Config:
        from_attributes = True
