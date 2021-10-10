from fastapi import APIRouter, Depends

from ..security import get_current_user, OauthUser
from ..scraper.parent import Parent
from ..scraper.student import Student

router = APIRouter(tags=["User"])


@router.get("/get_all/")
async def get_all(userDetails: OauthUser = Depends(get_current_user)):
    # TODO: This does not currently work. Need to hook up to SQL
    # TODO: For JWT also add a parent or student attribute.
    if userDetails["student"]:
        user = Student(userDetails["username"])
    else:
        user = Parent(userDetails["username"])
    return await user.get_all()
