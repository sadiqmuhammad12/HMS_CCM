
from pageObject.pages.basePage import basePage
from pageObject.pages.locators.Dlete_Chronic_Condition.delete_Chronic_Condition import Locators




class delete_chronic_condition(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(searchpage.base_url)

    def do_delete_chronic_condition(self,):
             self.do_click(Locators.deleteChronicConditionbtn)
             self.do_click(Locators.deletefull)
             return True