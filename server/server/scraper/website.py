import requests
from bs4 import BeautifulSoup

from ..config import DISTRICT_CODE, DISTRICT_CODE_URL


class Website:
    def __init__(self, email) -> None:
        # Init values
        self.districtCode = DISTRICT_CODE
        self.email = email
        self.baseURL = f"https://{DISTRICT_CODE_URL}.client.renweb.com/pwr"
        self.session = requests.session()
        self.baseData = {
            "DistrictCode": self.districtCode,
            "email": self.email,
        }

    def create_account(self) -> str:
        # The server uses this data to create a new account
        data = {**self.baseData, "login": "Create+Account"}
        # Post the data
        page = self.session.post(f"{self.baseURL}/create-account.cfm", data=data)
        # Put the page into bs4
        soup = BeautifulSoup(page.text, "lxml")
        # Make bs4 find the response (the class name is misleading)
        resp = soup.find("h3", {"class": "loginerror"}).text.strip()
        # We return the response
        return resp

    def forgot_credentials(self) -> str:
        # Data that will be sent to reset password
        data = {
            **self.baseData,
            "login": "Reset+Password",
        }
        page = self.session.post(f"{self.baseURL}/forgot-login.cfm", data=data)
        # Put the page into bs4
        soup = BeautifulSoup(page.text, "lxml")
        # Make bs4 find the response (the class name is misleading)
        resp = soup.find("h3", {"class": "loginerror"}).text.strip()
        # Return response
        return resp


print(Website("parinzee@gmail.com").forgot_credentials())
