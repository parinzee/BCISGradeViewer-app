from fastapi import APIRouter

from ..dependencies import oauthSchemeDependecy
from ..scraper.user import User

router = APIRouter()


@router.get("/get_all")
async def get_all(token: str = oauthSchemeDependecy):
    return {"token": token}
