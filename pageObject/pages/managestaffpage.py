from pageObject.pages.basePage import basePage
from pageObject.pages.locators.managestafflocators.manageStafflocators import Locators
from pageObject.config.manage_Staff import test_staff_data
from selenium.webdriver.support.ui import Select
import time


class managestaffForm(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(testData.base_url)

    def do_managestaff(self, ccfirstname, cclastname, ccUsername, ccPass, ccCpass, ccEmail, ccAlertEmail,
                       ccContactno, clinicianRole, cccity, clinician_zip_first):
        self.do_click(Locators.manage_staff_btn)
        time.sleep(2)
        self.do_click(Locators.add_staff_btn)
        time.sleep(2)
        self.do_send_keys(Locators.clinician_first_name, ccfirstname)
        self.do_send_keys(Locators.clinician_last_name, cclastname)
        self.do_send_keys(Locators.clinician_username, ccUsername)
        self.do_send_keys(Locators.clinician_password, ccPass)
        self.do_send_keys(Locators.clinician_password, ccCpass)
        self.do_send_keys(Locators.clinician_email, ccEmail)
        self.do_send_keys(Locators.clinician_alert_mail, ccAlertEmail)
        self.do_send_keys(Locators.clinician_phone_number, ccContactno)
        self.do_send_keys(Locators.select_role, clinicianRole)
        dropdown_element = self.driver.find_element(*Locators.select_role)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text('Clinician')

        self.do_send_keys(Locators.clinician_city, cccity)

        self.do_click(Locators.select_state)
        dropdown_element = self.driver.find_element(*Locators.select_state)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text('Colorado')

        self.do_send_keys(Locators.clinician_zip_first,clinician_zip_first)

        # Example 2: Select by value
        # dropdown_element = driver.find_element(*locators.ccstate)
        # dropdown = Select(dropdown_element)
        # dropdown.select_by_value(ccstate)
