from fastapi import APIRouter, Depends

from ..dependencies import get_current_user, oauthScheme, OauthUser
from ..scraper.user import User

router = APIRouter(tags=["User"])


@router.get("/me/")
async def get_current_user(current_user: OauthUser):
    return current_user


@router.get("/get_all/")
async def get_all(token: str = Depends(oauthScheme)):
    return {"token": token}
