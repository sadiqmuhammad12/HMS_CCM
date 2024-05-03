
from pageObject.pages.basePage import basePage
from pageObject.pages.locators.edit_chronic_condition.edit_chronic_condition import Locators




class edit_chronic_condition(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(edit_chronic_condition.base_url)

    def do_edit_chronic_condition(self,edit_input_field):
             self.do_click(Locators.editChronicConditionbtn)
             self.do_click(Locators.edit_input_field)
             self.do_send_keys(Locators.edit_input_field,edit_input_field)
             self.do_click(Locators.save_btn)
             return True
