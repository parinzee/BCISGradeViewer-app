from fastapi import APIRouter, Depends

from ..security import get_current_user, OauthUser
from ..scraper.user import User

router = APIRouter(tags=["User"])


@router.get("/get_all/")
async def get_all(userDetails: OauthUser = Depends(get_current_user)):
    # TODO: This does not currently work. Need to hook up to SQL
    user = User(userDetails["username"])
    return await user.get_all()
