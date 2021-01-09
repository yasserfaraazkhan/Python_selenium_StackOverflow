from configuration.BaseClass import *

class Selenium(BaseClass):
    driver = None
    _timeout = 10

    def __init__(self, driver):
        self.driver = self.getDriver()

    def find_element(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def get_text(self, locator):
        return self.find_element(locator).text

    def find_elements(self, locator):
        return self.driver.find_elements(locator["by"], locator["value"])

    def find_element_by_index(self, locator, index):
        return self.driver.find_elements(locator["by"], locator["value"])[index]

    def enter_text(self, locator, input_string):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(input_string)

    def click_element(self, locator):
        self.driver.find_element(locator["by"], locator["value"]).click()

    # get a particular element from list of elements
    def find_from_elements(self, locator, index):
        return self.find_elements(locator)[index]

    def get_url(self, url):
        self.driver.get(url)
