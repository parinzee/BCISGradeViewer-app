import asyncio
from server.dependencies import get_current_user
from server.exceptions import CredentialsException
from jose import jwt, JWTError

from fastapi.testclient import TestClient
from server.main import app
from os import environ
from server.config import SECRET_KEY, ALGORITHM

client = TestClient(app)


# Get a valid username & password to test against from ENV variables
username = environ["GV_TEST_USERNAME"]
password = environ["GV_TEST_PASSWORD"]
student = environ[
    "GV_TEST_STUDENT"  # false or true
]  # Is the account for testing a student or a parent's?


def test_not_allowed():
    # Try accessing a path that requires login
    response = client.get("/user/dashboard/")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}

    # Try feeding wrong user details
    response = client.post(
        "/token/?student=false",
        {
            "grant_type": None,
            "username": "foo",
            "password": "bar",
            "scope": None,
            "client_id": None,
            "client_secret": None,
        },
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


def test_get_current_user():
    loop = asyncio.get_event_loop()

    # Test bad JWT
    token = "eyJhbGciOiIJUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJUaGFueWFsdWsiLCJleHAiOjE2MzUwNjc3MjR9.lTXOczPQ27J1hmnueImlqQcod1sCucrgkqRigA6BH44"

    try:
        loop.run_until_complete(get_current_user(token))
        assert False
    except type(CredentialsException):
        assert True

    # Test good JWT
    response = client.post(
        f"/token/?isStudent={student}",
        {
            "grant_type": None,
            "username": username,
            "password": password,
            "scope": None,
            "client_id": None,
            "client_secret": None,
        },
    )

    # Get the correct JWT
    token = response.json()["access_token"]
    decodedToken = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert username == decodedToken.get("sub")
