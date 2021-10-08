from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

# Depends on the oauth scheme
oauthScheme = OAuth2PasswordBearer(tokenUrl="token")
oauthSchemeDependecy = Depends(oauthScheme)
