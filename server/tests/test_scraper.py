import asyncio
from os import environ
from server.scraper.parent import Parent
from server.scraper.student import Student
from server.scraper.website import Website
from random import randint

# Get the username, password, and student id to test against from ENV variables
username = environ["GV_TEST_USERNAME"]
password = environ["GV_TEST_PASSWORD"]
studentID = int(environ["GV_TEST_STUDENTID"])
student = environ["GV_TEST_STUDENT"]

# Tests the Connectivity
def test_connectivity():
    # Establishes connection
    if student == "false":
        user = Parent(username, password)
    else:
        user = Student(username, password)
    # Test deletion
    del user
    assert True


def test_methods():
    if student == "false":
        user = Parent(username, password)
    else:
        user = Student(username, password)
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


def test_website():
    # This tests the reset password functionality
    web = Website("foo@bar.com")
    assert (
        web.forgot_credentials()
        == "If a valid email address was found, an email has been sent with instructions for how to reset your password."
    )
    assert (
        web.create_account()
        == "An email has been sent to foo@bar.com with instructions for how to create a Family Portal login."
    )
