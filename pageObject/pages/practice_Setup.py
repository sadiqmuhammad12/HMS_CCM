from pageObject.pages.basePage import basePage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.pages.locators.Console_locators.Console_locators import locators
from pageObject.pages.locators.practice_SetupConfig.practice_Setupconfig import locators



class do_practice_setup_Page(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(console_Data.base_url)

    def do_practice_setup(self):
        self.do_click(locators.practice_Setupbtn)




