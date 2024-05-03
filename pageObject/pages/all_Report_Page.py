from pageObject.pages.basePage import basePage
from pageObject.pages.locators.all_Report_Locator.all_Report_Locator import locators
import time

from pageObject.config.search_Config import search_Data


class all_Report_page(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(console_Data.base_url)

    def do_All_Report(self):
        self.do_click(locators.all_Report_btn)
        time.sleep(6)
        self.do_click(locators.all_Report_Download_btn)
        time.sleep(6)
        pass


