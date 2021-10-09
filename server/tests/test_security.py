import asyncio
from server.security import get_current_user
from server.exceptions import CredentialsException

from fastapi.testclient import TestClient
from server.main import app
from os import environ

client = TestClient(app)


# Get a valid username & password to test against from ENV variables
username = environ["GV_USERNAME"]
password = environ["GV_PASS"]


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
        "/token/",
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
    # Try sending it to get_current_user
    response = client.get("/token/me/", headers={"Authorization": f"Bearer {token}"})
    assert response.json()["username"] == username
