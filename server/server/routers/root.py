from fastapi import APIRouter, Depends

from ..security import get_current_user, OauthUser
from ..scraper.parent import Parent
from ..scraper.student import Student
from ..sql.crud import get_user
from ..dependencies import get_db

from sqlalchemy.orm import Session

router = APIRouter(tags=["User"], prefix="/user")


@router.get("/get_all/")
async def get_all(
    userDetails: OauthUser = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    userInDB = get_user(db, userDetails.username, userDetails.student)
    if userDetails.student:
        user = Student(userDetails.username, userInDB.password)
    else:
        user = Parent(userDetails.username, userInDB.password)
    return await user.get_all()
