from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from ..security import get_current_user, OauthUser, create_access_token
from ..scraper.user import User
from ..exceptions import NotAuthenticated

router = APIRouter(tags=["Token"], prefix="/token")

# Gets the current user
@router.get("/me/")
async def get_curr_user(current_user: OauthUser = Depends(get_current_user)):
    return current_user


@router.post("/")
async def login(formData: OAuth2PasswordRequestForm = Depends()):
    # TODO: If user exists in database, don't waste time connecting to servers.
    try:
        User(formData.username, formData.password)
    except NotAuthenticated:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token({"sub": formData.username})

    return {"access_token": access_token, "token_type": "bearer"}
