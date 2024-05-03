from selenium.webdriver.support.select import Select

from pageObject.pages.basePage import basePage
from pageObject.pages.locators.signuppagelocators.signuppagelocators import signup_locators
import time
from pageObject.config.signup_config import signup_testData


class SignupPage(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(signup_testData.base_url)

    def do_Signup(self, practicename, practiceaddress1, practiceaddress2, Country, city, Zip, providerfirstname,
                  providerlastname, username, email, AlertEmail, contactno, Pass, Cpass):
        self.do_click(signup_locators.signupbtn)
        self.do_send_keys(signup_locators.PracticeName, practicename)
        time.sleep(4)
        self.do_send_keys(signup_locators.PracticeAddress1, practiceaddress1)
        time.sleep(4)
        self.do_send_keys(signup_locators.PracticeAddress2, practiceaddress2)
        time.sleep(4)
        self.do_send_keys(signup_locators.City, city)

        time.sleep(4)
        self.do_click(signup_locators.SelectState)
        time.sleep(4)

        self.do_click(signup_locators.state_value)
        # dropdown_element = self.driver.find_element(*signup_locators.SelectState)
        # dropdown = Select(dropdown_element)
        # dropdown.select_by_visible_text('Colorado')
        time.sleep(4)
        self.do_send_keys(signup_locators.Zip, Zip)
        time.sleep(4)
        self.do_click(signup_locators.SelectDesignation)
        dropdown_element = self.driver.find_element(*signup_locators.SelectDesignation)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text('MD')
        time.sleep(4)
        self.do_send_keys(signup_locators.ProviderFirstName, providerfirstname)
        time.sleep(4)
        self.do_send_keys(signup_locators.ProviderLastName, providerlastname)
        time.sleep(4)
        self.do_send_keys(signup_locators.UserName, username)
        time.sleep(4)
        self.do_send_keys(signup_locators.Email, email)
        time.sleep(4)
        self.do_send_keys(signup_locators.AlertMail, AlertEmail)
        time.sleep(4)
        self.do_send_keys(signup_locators.PhoneNumber, contactno)
        time.sleep(4)

        self.do_send_keys(signup_locators.password, Pass)
        time.sleep(4)
        self.do_send_keys(signup_locators.ConfirmPass, Cpass)
        time.sleep(4)
        # self.do_click(signup_locators.captcha)
        # time.sleep(4)
        self.do_click(signup_locators.checkbox)
        time.sleep(4)

        self.do_click(signup_locators.submitbtn)
        time.sleep(3)
