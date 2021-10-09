from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm

from ..security import get_current_user, OauthUser, create_access_token
from ..scraper.user import User
from ..exceptions import NotAuthenticated
from ..dependencies import get_db
from ..sql import crud, schemas
from sqlalchemy.orm import Session

router = APIRouter(tags=["Token"], prefix="/token")

# Gets the current user at /token/me
@router.get("/me/")
async def get_curr_user(current_user: OauthUser = Depends(get_current_user)):
    return current_user


# Login at /token/
@router.post("/")
def login(
    student: bool,
    backgroundTask: BackgroundTasks,
    formData: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    # Check if user already exists in db
    user = crud.get_user(db, formData.username, student)
    if user == None:
        # If they don't then perform validation
        try:
            User(formData.username, formData.password)
            # TODO: Queue a background task to add the user to the database
        except NotAuthenticated:
            raise HTTPException(
                status_code=401, detail="Incorrect username or password"
            )
    # Give user the access token
    access_token = create_access_token({"sub": formData.username})

    return {"access_token": access_token, "token_type": "bearer"}
