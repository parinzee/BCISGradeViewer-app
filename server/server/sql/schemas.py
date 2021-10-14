from typing import Optional, List
from pydantic import BaseModel

# For more info see fastapi documentation: https://fastapi.tiangolo.com/tutorial/sql-databases/
class UserBase(BaseModel):
    username: str
    password: str


class ParentCreate(UserBase):
    pass


class Parent(UserBase):
    id: int

    class Config:
        orm_mode = True


class StudentCreate(UserBase):
    username: Optional[str] = None
    password: Optional[str] = None


class Student(StudentCreate):
    id: int
    password: str
    student_id: int
    classes: List[dict]

    class Config:
        orm_mode = True
