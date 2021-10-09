from fastapi.responses import ORJSONResponse
from os import environ

### SCRAPER SETTINGS ###
DISTRICT_CODE = "BC-THA"  # Sets district code for accessing renweb. If self-deploying you may have to change this.
DISTRICT_CODE_URL = DISTRICT_CODE.lower()


### SERVER SETTINGS ###
JSON_RESPONSE = ORJSONResponse  # Response type. See fastapi docs https://fastapi.tiangolo.com/advanced/custom-response/ for availble values.

### Oauth2 Settings ###
ACCESS_TOKEN_EXPIRE_DAYS = 15  # Time before Oauth2 token expires.
ALGORITHM = "HS256"  # Algorithm for signing JWT
SECRET_KEY = environ["GV_SECRET"]  # Key to sign JWT tokens (run: openssl rand -hex 32)
FERNET_KEY = environ["GV_FERNET"]  # Encrypt password with Fernet. (generate key first)
