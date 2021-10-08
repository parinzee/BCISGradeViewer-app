from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from ..scraper.user import User
from ..exceptions import NotAuthenticated

router = APIRouter(tags=["Token"], prefix="/token")


@router.post("/")
async def login(formData: OAuth2PasswordRequestForm = Depends()):
    try:
        User(formData.username, formData.password)
    except NotAuthenticated:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": formData.username, "token_type": "bearer"}
