import asyncio
import re
from typing import Dict, List

import requests
from bs4 import BeautifulSoup

from ..config import districtCode, districtCodeUrl
from ..exceptions import NotAuthenticated


class User:
    """
    Scrape data from user account.
    """

    def __init__(
        self, username: str, password: str, userType: str = "PARENTSWEB-PARENT"
    ) -> None:
        """
        Takes in Username and Password of Account
        """
        # Initialize values
        self.username = username
        self.password = password
        self.districtCode = districtCode
        self.userType = userType
        self.baseURL = f"https://{districtCodeUrl}.client.renweb.com/pwr"
        self.session = requests.session()

        # Perform authentication
        self._auth()

    def __del__(self) -> None:
        self.session.close()

    def _login(self):
        """Not to be confused with _auth which handles logging in successfully, _login only logs in."""
        # Set parameters
        submit = "Login"
        formMethod = "login"

        # Data that will be sent to authenticate.
        login_data = {
            "DistrictCode": self.districtCode,
            "UserName": self.username,
            "Password": self.password,
            "UserType": self.userType,
            "Submit": submit,
            "formMethod": formMethod,
        }

        # Post the login data to attempt to authenticate
        self.session.post(self.baseURL + "/", data=login_data)

    def _auth(self) -> None:
        """
        Authentication Method which authenticates the user with the Renweb Servers.
        """

        # Firstly Login
        self._login()

        # Set url and check it. If not redirected, then it means that we are authenticated.
        url = self.session.get(f"{self.baseURL}/student/index.cfm")
        if url.url != f"{self.baseURL}/student/index.cfm":
            raise NotAuthenticated()

    def get_events(self) -> List[Dict[str, str]]:
        """
        Gets the events for the school year.
        """
        # Pull in page data and parse it
        page = self.session.get(f"{self.baseURL}/school/").text

        # Store events
        eventList = []

        # Parse and get events
        soup = BeautifulSoup(page, "lxml")
        parsedEvents = soup.find(id="school_events").find("tbody").find_all("tr")

        for rows in parsedEvents:
            # For each row, find all the data in each table (td)
            tds = rows.find_all("td")

            # Get dates and events in text form
            date = [i.text for i in tds]

            # Strip out tabs, newlines, and tabs again. This has been the most effective method.
            date, title = list(
                map(lambda event: event.strip("\t").strip("\n").strip("\t"), date)
            )

            # Date variable will be a list of dates and events ["12/12/2021", "Future"]
            # Change that into a dictionary and apppend into variable for storing events
            event = {title: date}
            eventList.append(event)

        return eventList

    def get_studentIDs(self) -> List[str]:
        """
        Get all the students that the parents have.
        """
        # Variable to store ids
        studentIDList = []

        page = self.session.get(f"{self.baseURL}/student/index.cfm").text

        # Use BeautifulSoup to parse the web page
        page = BeautifulSoup(page, "lxml")

        # Find the tables storing links to gradebook.
        select = page.find("select", {"id": "classes_student_select"})

        for studentID in select.find_all("option"):
            studentIDList.append(studentID["value"])

        return studentIDList

    def get_subjects(self, studentID: int = None) -> List[dict]:
        """
        Get all the subjects for the specified studentID. If unspecified, will fetch subjects for all studentIDs for the user.
        """

        # Initialize list for storing urls
        classes = []

        # Access the Page
        page = self.session.get(f"{self.baseURL}/student/index.cfm").text
        page = BeautifulSoup(page, "lxml")

        # Find the tables which store links to the gradebook.
        tables = page.find_all("table")

        for table in tables:
            for tableBody in table.find_all("tbody"):
                # Process is below is to find the subject names and grade
                subjectsAndGrade = []
                subjects = [i.text.strip("\n") for i in tableBody.find_all("td")]
                for index in range(len(subjects)):
                    if index % 3 == 0:
                        subjectsAndGrade.append(
                            {
                                "className": subjects[index],
                                "score": subjects[index + 1],
                                "teacher": subjects[index + 2],
                            }
                        )
                # Find every row in the table body
                for tr in tableBody.find_all("tr"):
                    # Find all link tags (<a>) that links to the specifc *grades.cfm document* that gradebooks are stored using regex
                    for link in tr.findAll(
                        "a", attrs={"href": re.compile("^grades.cfm")}
                    ):

                        # For each <a> tag get the href that has the actuall link
                        link: str = link.get("href")
                        linkStudentID, linkClassID, linkTermID = link.split("?")[
                            1
                        ].split("&")
                        if studentID != None and studentID != int(
                            linkStudentID.split("=")[1]
                        ):
                            next
                        else:
                            classes.append(
                                {
                                    "studentID": int(linkStudentID.split("=")[1]),
                                    "classID": int(linkClassID.split("=")[1]),
                                    "termID": int(linkTermID.split("=")[1]),
                                }
                            )

                # Merge the two dictionaries in order to get the complete className, classID, and grades.
                for subjectAndGrade, subject in zip(subjectsAndGrade, classes):
                    subject["className"] = subjectAndGrade["className"]
                    subject["score"] = subjectAndGrade["score"]

        return classes

    def get_subject_grade_book(self, studentID: int, classID: int, termID: int) -> str:
        """
        Gets the html of the specified gradebook
        """
        return self.session.get(
            f"{self.baseURL}/NAScopy/Gradebook/GradeBookProgressReport-PW.cfm?District={self.districtCode}&StudentID={studentID}&ClassID={classID}&TermID={termID}&SchoolCode={self.districtCode.split('-')[0]}"
        ).text

    async def get_all(self):
        """
        Method to retrieve: events, studentIDs, and subjects asynchronously.
        """
        loop = asyncio.get_running_loop()
        events, studentIDs, subjects = await asyncio.gather(
            loop.run_in_executor(None, self.get_events),
            loop.run_in_executor(None, self.get_studentIDs),
            loop.run_in_executor(None, self.get_subjects),
        )

        return {"events": events, "studentIDs": studentIDs, "subjects": subjects}
