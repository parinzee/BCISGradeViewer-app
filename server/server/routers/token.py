from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm

from ..security import create_access_token
from ..dependencies import get_db
from ..scraper.parent import Parent
from ..scraper.student import Student
from ..exceptions import IncorrectCredentialsException, NotAuthenticated
from ..sql import crud, schemas
from ..scraper.parent import Parent
from ..scraper.student import Student
from sqlalchemy.orm import Session

router = APIRouter(tags=["Token"], prefix="/token")

# Login at /token/
@router.post("/")
def login(
    backgroundTask: BackgroundTasks,
    isStudent: bool = False,
    formData: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    # Check if user already exists in db
    print(isStudent)
    user = crud.get_user(db, formData.username, isStudent)
    if user == None:
        # If they are not in our database, verify.
        try:
            # TODO: Queue a background task to add the user to the database
            if isStudent:
                Student(formData.username, formData.password)
                # Bottom code will only run if password is correct, otherwise it will be caught by the except below.
                backgroundTask.add_task(
                    crud.create_student,
                    db,
                    schemas.StudentCreate(
                        username=formData.username,
                        password=formData.password,
                    ),
                )
            else:
                Parent(formData.username, formData.password)
                backgroundTask.add_task(
                    crud.create_parent,
                    db,
                    schemas.ParentCreate(
                        username=formData.username, password=formData.password
                    ),
                )
        except NotAuthenticated:
            raise IncorrectCredentialsException

    # IF they do exist, make sure that the passwords match.
    if user and user.password != formData.password:
        raise IncorrectCredentialsException

    # Give user the access token
    access_token = create_access_token(
        {"sub": formData.username, "isStudent": isStudent}
    )

    return {"access_token": access_token, "token_type": "bearer"}
