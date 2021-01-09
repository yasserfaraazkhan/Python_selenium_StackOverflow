import sys, pytest
from selenium.webdriver.support.ui import WebDriverWait
import config

@pytest.mark.usefixtures("setup")
class BaseClass():

    wait = None
    url = None

    def getDriver(self):
        return self.driver

    def getWait(self):
        if self.wait is None:
            self.wait = WebDriverWait(self.getDriver(), 10)
        return self.wait
