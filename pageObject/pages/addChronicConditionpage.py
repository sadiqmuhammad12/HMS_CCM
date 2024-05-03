from pageObject.pages.basePage import basePage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.pages.locators.searchLocator import locators
from pageObject.pages.locators.add_ChronicCondition_locator.add_Chronic_Condition_locator import Locators
from pageObject.pages.practice_Setup import do_practice_setup_Page
from pageObject.pages.locators.Console_locators.Console_locators import locators
from pageObject.config.search_Config import search_Data
import time

class do_add_ChronicCondition(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(searchpage.base_url)

    def do_addChronicCondition(self,chronicCondition):
        time.sleep(3)
        self.do_click(Locators.addChronicConditionbtn)
        time.sleep(3)
        self.do_send_keys(Locators.chronicCondition, chronicCondition)
        time.sleep(3)
        self.do_click(Locators.savebtn)




