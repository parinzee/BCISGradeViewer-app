from .parent import Parent
from ..config import DISTRICT_CODE, DISTRICT_CODE_URL
import requests


# Student inherits most properties from the parents. Except the few are changed below
class Student(Parent):
    def __init__(
        self,
        username: str,
        password: str,
    ) -> None:
        """
        Takes in Username and Password of Account
        """
        # Initialize values
        self.username = username
        self.password = password
        self.districtCode = DISTRICT_CODE
        self.userType = "PARENTSWEB-STUDENT"
        self.baseURL = f"https://{DISTRICT_CODE_URL}.client.renweb.com/pwr"
        self.session = requests.session()

        # Perform authentication
        self._auth()
