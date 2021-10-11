from typing import Optional, List
from pydantic import BaseModel

# For more info see fastapi documentation: https://fastapi.tiangolo.com/tutorial/sql-databases/
class UserBase(BaseModel):
    username: str


# This class for getting current user
class User(UserBase):
    student: bool


class ParentCreate(UserBase):
    password: str


class Parent(UserBase):
    id: int
    password: str

    class Config:
        orm_mode = True


class StudentCreate(UserBase):
    username: Optional[str] = None
    password: Optional[str] = None


class Student(StudentCreate):
    id: int
    password: str
    student_id: int
    parent: str
    classes: List[dict]

    class Config:
        orm_mode = True
