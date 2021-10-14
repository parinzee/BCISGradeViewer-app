from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from .database import Base


class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True)
    # Every parent has an account
    username = Column(String(30), nullable=False)
    password = Column(String, nullable=False)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    # Not every student has an account
    username = Column(String(30), nullable=True)
    password = Column(String, nullable=True)
    student_id = Column(Integer, nullable=False)
