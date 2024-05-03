from pageObject.pages.basePage import basePage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.pages.locators.searchLocator import locators
from pageObject.pages.locators.Console_locators.Console_locators import locators
from pageObject.config.search_Config import search_Data


class do_Search_Page(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(searchpage.base_url)

    def do_Search(self, search):
        self.do_send_keys(locators.search , search)
        self.do_click(locators.searchbtn)

    def do_Patientconsole(self):
        self.do_click(locators.patientBtn)




