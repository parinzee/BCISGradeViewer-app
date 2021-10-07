from os import environ
from server.scraper.user import User

# Get the username, password, and student id to test against from ENV variables
username = environ["GV_USERNAME"]
password = environ["GV_PASS"]
studentID = int(environ["GV_STUDENTID"])

# Tests the Connectivity
def test_connectivity():
    User(username, password)
    assert True


def test_get_events():
    assert len(User(username, password).get_events()) != []


def test_get_studentIDs():
    assert len(User(username, password).get_studentIDs()) != []


def test_get_subjects_all():
    assert len(User(username, password).get_subjects_all()) != []


def test_get_subject_one():
    assert len(User(username, password).get_subject_one(studentID)) != []
