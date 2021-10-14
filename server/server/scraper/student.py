from .parent import Parent
from bs4 import BeautifulSoup

# Student inherits most properties from the parents. Except the few are changed below
class Student(Parent):
    def __init__(
        self,
        username: str,
        password: str,
    ) -> None:
        """
        Takes in Username and Password of a students account. Inherits from Parent.
        """
        # Inherits from parents but instead passes PARENTSWEB-STUDENT
        super().__init__(username, password, "PARENTSWEB-STUDENT")

    def get_studentIDs(self) -> int:
        """
        Get all the students that the parents have.
        """

        page = self.session.get(f"{self.baseURL}/student/index.cfm").text

        # Use BeautifulSoup to parse the web page
        page = BeautifulSoup(page, "lxml")

        # Find the tables storing links to gradebook.
        select = page.find("select", {"id": "classes_student_select"})

        return int(
            select.find("option")["value"]
        )  # Student accounts are guranteed to have one ID.
