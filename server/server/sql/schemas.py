from typing import Optional, List
from pydantic import BaseModel

# For more info see fastapi documentation: https://fastapi.tiangolo.com/tutorial/sql-databases/
class ParentBase(BaseModel):
    username: str
    password: str


class ParentCreate(ParentBase):
    pass


class Parent(ParentBase):
    id: int

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int
    student_id: int
    parent: str
    classes: List[dict]

    class Config:
        orm_mode = True
