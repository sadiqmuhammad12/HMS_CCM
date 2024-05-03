import time
from pageObject.pages.basePage import basePage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.pages.locators.searchLocator import locators
from pageObject.pages.locators.Console_locators.Console_locators import locators
from pageObject.pages.locators.searchCC.searchCC_locator import Locators
from pageObject.pages.locators.search_chronic_condition.search_chronic_condition import Locators
from pageObject.pages.locators.Dlete_Chronic_Condition.delete_Chronic_Condition import Locators
from pageObject.pages.locators.add_ChronicCondition_locator.add_Chronic_Condition_locator import Locators
from pageObject.pages.locators.simple_search_chronic_condition.simple_search_chronic_condition import simple_search_locators
from pageObject.config.search_Config import search_Data


class simple_search_chronic_conditions(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(searchpage.base_url)

    def do_simple_search(self, input_data):
        self.do_click(simple_search_locators.search_bar)
        self.do_send_keys(simple_search_locators.input_data, input_data)
        self.do_click(simple_search_locators.search_bar_btn)
        time.sleep(3)
        self.do_click(Locators.searchCCbtn)


