import asyncio
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


def test_methods():
    user = User(username, password)
    assert user.get_events() != []

    assert user.get_studentIDs() != []

    assert user.get_subjects() != []

    subjects = user.get_subjects(studentID)
    assert subjects != []
    for subject in subjects:
        assert subject["studentID"] == studentID

    # Test get_subject_grade_book
    index = randint(0, len(subjects) - 1)
    selectedSubject = subjects[index]
    response = user.get_subject_grade_book(
        selectedSubject["studentID"],
        selectedSubject["classID"],
        selectedSubject["termID"],
    )
    # Make sure the html returned has that class name is not a 500 Error
    assert (
        selectedSubject["className"] in response
        and "500 - Internal server error." not in response
    )

    # Test get_all
    loop = asyncio.get_event_loop()
    # Run in the event loop
    data = loop.run_until_complete(asyncio.gather(user.get_all()))[0]

    # Make sure the dictionaries are not empty.
    assert data["events"] != []
    assert data["studentIDs"] != []
    assert data["subjects"] != []
