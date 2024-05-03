from pageObject.pages.basePage import basePage
from pageObject.pages.locators.patient_Logs.patient_Logs_Locators import Locators
import time

from pageObject.config.search_Config import search_Data


class patient_Logs_page(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(console_Data.base_url)

    def do_Patient_Logs(self,description):
        self.do_click(Locators.patient_Logs_btn)
        time.sleep(6)
        self.do_click(Locators.edit)
        self.do_send_keys(Locators.description,description)
        time.sleep(2)
        self.do_click(Locators.save_bttn)
        pass


