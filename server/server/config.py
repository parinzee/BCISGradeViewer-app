from fastapi.responses import ORJSONResponse
from os import environ

### SCRAPER SETTINGS ###
DISTRICT_CODE = environ["GV_DISTRICT_CODE"]  # Code for accessing renweb. Ex: BC-THA
DISTRICT_CODE_URL = DISTRICT_CODE.lower()


### SERVER SETTINGS ###
JSON_RESPONSE = ORJSONResponse  # Response type. See fastapi docs https://fastapi.tiangolo.com/advanced/custom-response/ for availble values.

### Oauth2 SETTINGS ###
SECRET_KEY = environ["GV_SECRET"]  # Key to sign JWT tokens (run: openssl rand -hex 32)
FERNET_KEY = environ["GV_FERNET"]  # Encrypt password with Fernet. (generate key first)
ACCESS_TOKEN_EXPIRE_DAYS = None  # Time before Oauth2 token expires, setting to None because a mobile app stays logged in.
ALGORITHM = "HS256"  # Algorithm for signing JWT

### SQL SETTINGS ###
DATABASE_URL = environ["DATABASE_URL"]  # Get postgres url from heroku deployment
