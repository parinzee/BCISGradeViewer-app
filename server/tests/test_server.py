from server import __version__
from fastapi.testclient import TestClient
from server.main import app
from os import environ

client = TestClient(app)


# Get a valid username & password to test against from ENV variables
username = environ["GV_TEST_USERNAME"]
password = environ["GV_TEST_PASSWORD"]
student = environ[
    "GV_TEST_STUDENT"  # false or true
]  # Is the account for testing a student or a parent's?


def test_version():
    assert __version__ == "0.1.0"


def test_root_get_all():
    response = client.post(
        f"/token/?student={student}",
        {
            "grant_type": None,
            "username": username,
            "password": password,
            "scope": None,
            "client_id": None,
            "client_secret": None,
        },
    )

    # Get JWT
    token = response.json()["access_token"]

    # Try sending it to get_current_user
    response = client.get(
        "/user/dashboard/", headers={"Authorization": f"Bearer {token}"}
    )

    data = response.json()
    # Make sure the dictionaries are not empty.
    assert data["events"] != []
    assert data["studentIDs"] != []
    assert data["subjects"] != []
