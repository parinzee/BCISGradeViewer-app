from server import __version__
from fastapi.testclient import TestClient
from server.main import app
from os import environ

client = TestClient(app)


# Get a valid username & password to test against from ENV variables
username = environ["GV_USERNAME"]
password = environ["GV_PASS"]


def test_version():
    assert __version__ == "0.1.0"


def test_authorization():
    # Try accessing a path that requires login
    response = client.get("/get_all/")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}

    # Try feeding wrong user details
    response = client.post(
        "/token/",
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

    # Finally try the right user details
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
    jsonResponse: dict = response.json()
    assert response.status_code == 200
    assert "access_token" in jsonResponse and "token_type" in jsonResponse
