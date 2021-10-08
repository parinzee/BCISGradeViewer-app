from datetime import datetime, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import BaseModel

from .config import ACCESS_TOKEN_EXPIRE_DAYS, ALGORITHM, SECRET_KEY

# Depends on the oauth scheme
oauthScheme = OAuth2PasswordBearer(tokenUrl="token")

# Create a user class for oauth
class OauthUser(BaseModel):
    username: str
    password: str


# Oauth, gets current user by jwt decoding.
async def get_current_user(token: str = Depends(oauthScheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("name")
    password: str = payload.get("pass")
    return {"username": username, "password": password}


# Create access JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
