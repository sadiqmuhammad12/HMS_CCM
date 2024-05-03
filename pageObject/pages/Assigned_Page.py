from pageObject.pages.basePage import basePage
from pageObject.pages.locators.Assigned.un_assigned import locators
from pageObject.config.add_Patient import add_PatientData
import time
from selenium.webdriver.support.select import Select
import time
from pageObject.config.signup_config import signup_testData


class assignedPage(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(add_PatientData.base_url)

    def do_assignedPatient(self):


        self.do_click(locators.assigned_btn)