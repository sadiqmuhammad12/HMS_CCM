import time


from pageObject.pages.basePage import basePage
from pageObject.pages.locators.inactive_edit_Patient_locator.inactive_edit_Patient_locator import inactive_edit_Locators




class inactive_edit_Patient(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(edit_chronic_condition.base_url)

    def do_inactive_edit_Patient(self,first_Name,last_Name,DOB,phone_No,Email,Ins_policy,Adress):
             time.sleep(3)
             self.do_click(inactive_edit_Locators.Inactive_dash_btn)
             self.do_click(inactive_edit_Locators.inactive_edit_dot_btn)
             time.sleep(3)
             self.do_click(inactive_edit_Locators.inactive_edit_btn)
             time.sleep(3)
             self.do_send_keys(inactive_edit_Locators.first_Name,first_Name)
             time.sleep(3)
             self.do_send_keys(inactive_edit_Locators.last_Name,last_Name)
             time.sleep(3)
             self.do_send_keys(inactive_edit_Locators.DOB,DOB)
             time.sleep(3)
             self.do_click(inactive_edit_Locators.Gender)
             time.sleep(3)
             self.do_click(inactive_edit_Locators.Gender_Value)
             time.sleep(3)
             self.do_send_keys(inactive_edit_Locators.phone_No,phone_No)
             time.sleep(3)
             self.do_send_keys(inactive_edit_Locators.email,Email)
             time.sleep(3)
             self.do_click(inactive_edit_Locators.Language)
             time.sleep(3)
             self.do_click(inactive_edit_Locators.Language_Vlaue)
             time.sleep(3)
             self.do_click(inactive_edit_Locators.Insurance)
             time.sleep(3)
             self.do_click(inactive_edit_Locators.Insurance_Vlaue)
             time.sleep(3)
             self.do_send_keys(inactive_edit_Locators.insurance_policy,Ins_policy)
             time.sleep(3)
             self.do_send_keys(inactive_edit_Locators.Adress,Adress)
             time.sleep(3)
             self.do_click(inactive_edit_Locators.update_btn)


