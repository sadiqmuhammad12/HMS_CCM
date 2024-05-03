import time

from pageObject.config.searchCC import searchCC_Data
from pageObject.pages.basePage import basePage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.pages.locators.searchLocator import locators
from pageObject.pages.locators.Console_locators.Console_locators import locators
from pageObject.pages.locators.searchCC.searchCC_locator import Locators
from pageObject.pages.locators.search_chronic_condition.search_chronic_condition import Locators
from pageObject.pages.locators.Dlete_Chronic_Condition.delete_Chronic_Condition import Locators

from pageObject.pages.locators.add_ChronicCondition_locator.add_Chronic_Condition_locator import Locators
from pageObject.config.search_Config import search_Data


class manage_chronic_condition(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(searchpage.base_url)

    def do_addChronicCondition(self, chronicCondition):
        self.do_click(Locators.addChronicConditionbtn)
        self.do_send_keys(Locators.chronicCondition, chronicCondition)
        self.do_click(Locators.savebtn)

    def do_SearchCC(self, searchCC, editinput ):
        self.do_send_keys(Locators.searchCC, searchCC)
        time.sleep(3)
        self.do_click(Locators.searchCCbtn)
        time.sleep(3)
        self.do_click(Locators.editbtn)
        time.sleep(3)
        # self.do_send_keys(Locators.editCC, editbtn)

        time.sleep(3)

        self.do_send_keys(Locators.editinput, editinput)

        self.do_click(Locators.savebtn)



        # self.do_click(Locators.deletebtn)
        # self.do_click(Locators.deletebtn2))

        # self.driver.get(searchpage.base_url)

