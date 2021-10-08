from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from pydantic import BaseModel

# Depends on the oauth scheme
oauthScheme = OAuth2PasswordBearer(tokenUrl="token")

# Create a user class for oauth
class OauthUser(BaseModel):
    username: str


# Token decoder
def oauth_token_decoder(token: str):
    # TODO: Actual decoding here
    return OauthUser(
        username=token + "decoded",
    )


def oauth_token_encoder(password: str):
    # TODO: Actual security here
    return


# Oauth
async def get_current_user(token: str = Depends(oauthScheme)):
    return oauth_token_decoder(token)
