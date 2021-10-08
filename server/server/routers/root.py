from fastapi import APIRouter, Depends

from ..security import get_current_user, OauthUser
from ..scraper.user import User

router = APIRouter(tags=["User"])


# TODO: Return all values from scraper
@router.get("/get_all/")
async def get_all(userDetails: OauthUser = Depends(get_current_user)):
    user = User(userDetails["username"], userDetails["password"])
    return await user.get_all()
