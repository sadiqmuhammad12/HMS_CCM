import time


from pageObject.pages.basePage import basePage
from pageObject.pages.locators.Active_Patient.Active_Patient import active_Locators




class Active_Patient(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(edit_chronic_condition.base_url)

    def do_Active_Patient(self,active_Input):
             time.sleep(3)
             self.do_click(active_Locators.Active_Dash_btn)
             time.sleep(3)
             self.do_click(active_Locators.Active_Dot_btn)
             self.do_click(active_Locators.Active_btn)
             self.do_send_keys(active_Locators.Active_input,active_Input)
             self.do_click(active_Locators.Active_full_btn)



