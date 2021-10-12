from fastapi import APIRouter, Depends
from typing import Union

from ..dependencies import get_current_user
from ..scraper.parent import Parent
from ..scraper.student import Student


router = APIRouter(tags=["User"], prefix="/user")


@router.get("/dashboard/")
async def get_dasboard(
    user: Union[Parent, Student] = Depends(get_current_user),
):
    return await user.get_all()


@router.get("/events/")
async def get_events(
    user: Union[Parent, Student] = Depends(get_current_user),
):
    return user.get_events()


@router.get("/studentids/")
async def get_studentIDs(
    user: Union[Parent, Student] = Depends(get_current_user),
):
    return user.get_studentIDs()


@router.get("/subjects/")
async def get_subjects(
    user: Union[Parent, Student] = Depends(get_current_user), studentID: int = None
):
    return user.get_subjects(studentID)


@router.get("/subjects/gradebook")
async def get_subject_gradebook(
    studentID: int,
    classID: int,
    termID: int,
    user: Union[Parent, Student] = Depends(get_current_user),
):
    return user.get_subject_grade_book(studentID, classID, termID)
