import time


from pageObject.pages.basePage import basePage
from pageObject.pages.locators.inactive_Patient.inactive_Patient import inactive_Locators
from pageObject.pages.locators.inactive_Patient.inactive_Patient import inactive_Locators




class inactive_Patient(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(edit_chronic_condition.base_url)

    def do_inactive_Patient(self,inactive_Input):
             time.sleep(3)
             self.do_click(inactive_Locators.inactive_dot_btn)
             time.sleep(3)
             self.do_click(inactive_Locators.inactive_btn)
             self.do_send_keys(inactive_Locators.inactive_input,inactive_Input)
             self.do_click(inactive_Locators.inactive_full_btn)

