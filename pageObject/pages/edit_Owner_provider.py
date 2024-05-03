import time

from selenium.webdriver.support.select import Select

from pageObject.pages.basePage import basePage
from pageObject.pages.locators.edit_Owner_Provider.edit_Owner_Provider import Locators




class edit_Owner_Provider(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(edit_chronic_condition.base_url)

    def do_edit_Owner_Provider(self,first_Name,last_Name,user_Name,alert_Mail,phone_No,Adress,City,zip):
             self.do_click(Locators.edit_dots_btn)
             self.do_click(Locators.edit_OwnerP_btn)
             self.do_send_keys(Locators.first_Name,first_Name)
             self.do_send_keys(Locators.last_Name,last_Name)
             self.do_send_keys(Locators.user_Name,user_Name)
             self.do_send_keys(Locators.alert_Mail,alert_Mail)
             self.do_send_keys(Locators.phone_No,phone_No)
             self.do_send_keys(Locators.Adress,Adress)
             self.do_send_keys(Locators.City,City)
             self.do_click(Locators.select_state)
             time.sleep(4)
             self.do_click(Locators.value_select_state)
             self.do_send_keys(Locators.zip,zip)
             self.do_click(Locators.save_btn)

