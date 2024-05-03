from pageObject.pages.basePage import basePage
from pageObject.pages.locators.patient_status_Crud_Locators.patient_status_Crud_Locator import locators
from pageObject.config.manage_Staff import test_staff_data
from selenium.webdriver.support.ui import Select
import time


class patient_Status_Crud(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(testData.base_url)

    def do_Patient_Status_Crud(self):
        self.do_click(locators.patient_status_btn)
        time.sleep(2)
        # self.do_click(patient_Status_locators.inactive_button)
        self.do_click(locators.inactive_Btn)
        self.do_click(locators.delete_Btn)
        self.do_click(locators.delete_full_Btn)