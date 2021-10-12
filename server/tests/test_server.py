from server import __version__
from fastapi.testclient import TestClient
from server.main import app
from os import environ
from random import randint

client = TestClient(app)


# Get a valid username & password to test against from ENV variables
username = environ["GV_TEST_USERNAME"]
password = environ["GV_TEST_PASSWORD"]
student = environ[
    "GV_TEST_STUDENT"  # false or true
]  # Is the account for testing a student or a parent's?
studentID = int(environ["GV_TEST_STUDENTID"])  # One student id
token = ""


def test_version():
    assert __version__ == "0.1.0"


def test_user_get_dashboard():
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
    global token
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


def test_user_subjects_and_gradebook():
    global token
    response = client.get(
        f"/user/subjects/?{studentID}", headers={"Authorization": f"Bearer {token}"}
    )
    # Make sure that the list only have the ones from the student id sent.
    subjects = response.json()
    for subject in subjects:
        assert subject["studentID"] == studentID

    # Test getting the gradebook
    index = randint(0, len(subjects) - 1)
    selectedSubject = subjects[index]
    response = client.get(
        "/user/subjects/gradebook/?studentID={}&classID={}&termID={}".format(
            selectedSubject["studentID"],
            selectedSubject["classID"],
            selectedSubject["termID"],
        ),
        headers={"Authorization": f"Bearer {token}"},
    )
    # Make sure the html returned has that class name is not a 500 Error
    assert (
        selectedSubject["className"] in response.json()
        and "500 - Internal server error." not in response.json()
    )


def test_user_other_routes():
    global token
    routes = [
        "/user/events/",
        "/user/subjects/",
        "/subjects/gradebook",
    ]
    for route in routes:
        response = client.get(route, headers={"Authorization": f"Bearer {token}"})
        data = response.json()
        assert data != []
