from pageObject.pages.basePage import basePage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.config.config import testData


class loginPage(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(testData.base_url)

    def do_login(self, useremail, password):
        self.do_send_keys(locators.useremail, useremail)
        self.do_send_keys(locators.password, password)
        self.do_click(locators.loginbtn)

