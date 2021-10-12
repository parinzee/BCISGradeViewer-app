from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from cryptography.fernet import Fernet

from .config import ACCESS_TOKEN_EXPIRE_DAYS, ALGORITHM, SECRET_KEY, FERNET_KEY

# Depends on the oauth scheme
oauthScheme = OAuth2PasswordBearer(tokenUrl="token")

# Create Fernet class used in server/sql/crud.py
encryptor = Fernet(FERNET_KEY)

# Create access JWT
def create_access_token(data: dict):
    # Create shallow copy of data
    toEncode = data.copy()

    # Set expiry date, if not none.
    if ACCESS_TOKEN_EXPIRE_DAYS:
        expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
        toEncode.update({"exp": expire})
    encodedJWT = jwt.encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)
    return encodedJWT
