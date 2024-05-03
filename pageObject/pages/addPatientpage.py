from pageObject.pages.basePage import basePage
from pageObject.pages.locators.add_Patient.addPatientlocator import locators
from pageObject.config.add_Patient import add_PatientData
import time
from selenium.webdriver.support.select import Select
import time
from pageObject.config.signup_config import signup_testData


class addPatientPage(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(add_PatientData.base_url)

    def do_addPatient(self, ptsName1, ptsName2 , ptsPhone, ptsEmail, insPolicyno, Address,):

        self.do_send_keys(locators.firstName, ptsName1)
        time.sleep(2)
        self.do_send_keys(locators.lastName, ptsName2)
        self.do_click(locators.DOB)
        dropdown_element = self.driver.find_element(*locators.DOB)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text('12/03/1996')
        self.do_click(locators.Gender)
        dropdown_element = self.driver.find_element(*locators.Gender)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text('Male')
        self.do_send_keys(locators.patientName, ptsPhone)
        self.do_send_keys(locators.patientEmail, ptsEmail)
        self.do_click(locators.patientLanguage)
        dropdown_element = self.driver.find_element(*locators.patientLanguage)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text('Pashto')
        self.do_click(locators.patientInsurance)
        dropdown_element = self.driver.find_element(*locators.patientInsurance)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text('CareConnect')
        self.do_send_keys(locators.insurancepolicy, insPolicyno)
        self.do_send_keys(locators.Address, Address)
        self.do_click(locators.submitbtn)