from pageObject.pages.basePage import basePage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.pages.locators.Console_locators.Console_locators import locators
from pageObject.pages.locators.carePlan_locators.careplanlocators import locators
from pageObject.config.search_Config import search_Data


class do_carePlan_page(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(console_Data.base_url)

    def do_carePlan(self):
        self.do_click(locators.carePlanBtn)
        self.do_click(locators.carePan_timerbtn)




