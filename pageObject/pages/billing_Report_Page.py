from pageObject.pages.basePage import basePage
from pageObject.pages.locators.download_Billing_Report.download_Billing_Report_locator import locators
from pageObject.config.config import testData
import time

class billig_Report_age(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(testData.base_url)

    def do_billig_Report(self ,from_value,to_Value):

        self.do_click(locators.billing_Report_Btn)
        self.do_click(locators.select_Clinician)
        self.do_click(locators.selected_Value)
        self.do_send_keys(locators.from_Value, from_value)
        self.do_send_keys(locators.to_Value,to_Value)
        self.do_click(locators.downloadbtn)
        time.sleep(5)


