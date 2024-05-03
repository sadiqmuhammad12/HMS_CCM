from pageObject.pages.basePage import basePage
from pageObject.pages.locators.patient_Status_locators import patient_Status_locators
from pageObject.config.manage_Staff import test_staff_data
from selenium.webdriver.support.ui import Select
import time


class patient_Status(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(testData.base_url)

    def do_Patient_Status(self):
        self.do_click(patient_Status_locators.patient_Status_btn)
        time.sleep(2)
        # self.do_click(patient_Status_locators.inactive_button)
        self.do_click(patient_Status_locators.active_button)

