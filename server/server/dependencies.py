from .exceptions import CredentialsException
from .scraper.parent import Parent
from .scraper.student import Student
from .sql.database import SessionLocal
from .sql.crud import get_user
from fastapi import Depends
from jose import jwt, JWTError
from .config import ALGORITHM, SECRET_KEY
from .security import oauthScheme

# Dependency to get session for each request.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Oauth, gets current user by jwt decoding.
async def get_current_user(token: str = Depends(oauthScheme)):
    db = SessionLocal()
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise CredentialsException
    username: str = payload.get("sub")
    student: bool = payload.get("student")
    password: str = get_user(
        db, username, student
    ).password  # Fetch user from the database and get their password
    db.close()
    if student:
        return Student(username, password)
    else:
        return Parent(username, password)
