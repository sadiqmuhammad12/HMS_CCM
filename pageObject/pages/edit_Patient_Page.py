import time

from selenium.webdriver.support.select import Select

from pageObject.pages.basePage import basePage
from pageObject.pages.locators.edit_Patient.edit_Patient import Locators




class edit_Patient(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(edit_chronic_condition.base_url)

    def do_edit_Patient(self,first_Name,last_Name,DOB,phone_No,Email,Ins_policy,Adress):
             self.do_click(Locators.edit_Pdots_btn)
             self.do_click(Locators.edit_Patient_btn)
             self.do_send_keys(Locators.first_Name,first_Name)
             self.do_send_keys(Locators.last_Name,last_Name)
             self.do_send_keys(Locators.DOB,DOB)
             self.do_click(Locators.Gender)
             self.do_click(Locators.gender_Value)
             self.do_send_keys(Locators.phone_No,phone_No)
             self.do_send_keys(Locators.Email,Email)
             self.do_click(Locators.Language)
             self.do_click(Locators.language_Vlaue)
             self.do_click(Locators.Insurance)
             self.do_click(Locators.insurance_Value)
             self.do_send_keys(Locators.ins_Policy,Ins_policy)
             self.do_send_keys(Locators.Adress, Adress)
             self.do_click(Locators.Update_btn)

