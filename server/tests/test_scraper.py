from os import environ
from server.scraper.user import User
from random import randint

# Get the username, password, and student id to test against from ENV variables
username = environ["GV_USERNAME"]
password = environ["GV_PASS"]
studentID = int(environ["GV_STUDENTID"])

# Tests the Connectivity
def test_connectivity():
    # Establishes connection
    user = User(username, password)
    # Test deletion
    del user
    assert True


def test_get_events():
    assert User(username, password).get_events() != []


def test_get_studentIDs():
    assert User(username, password).get_studentIDs() != []


def test_get_subjects_all():
    assert User(username, password).get_subjects() != []


def test_get_subject_one():
    passing = True
    user = User(username, password)
    # Gets the subject for one student
    subjects = user.get_subjects(studentID)
    if subjects == []:
        passing = False
    assert passing

    for subject in subjects:
        # If other students exist also failed
        if subject["studentID"] != studentID:
            passing = False

    assert passing


def test_get_subject_grade_book():
    user = User(username, password)
    subjects = user.get_subjects(studentID)
    # Pick a random subject
    index = randint(0, len(subjects) - 1)
    selectedSubject = subjects[index]
    response = user.get_subject_grade_book(
        selectedSubject["studentID"],
        selectedSubject["classID"],
        selectedSubject["termID"],
    )

    assert (
        selectedSubject["className"] in response
        and "500 - Internal server error." not in response
    )
