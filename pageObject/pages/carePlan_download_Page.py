from pageObject.pages.basePage import basePage
from pageObject.pages.locators.carePlan_Download.carePlan_Download import locators
import time

from pageObject.config.search_Config import search_Data


class do_carePlan_Download_page(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(console_Data.base_url)

    def do_CarePlan_download(self):
        self.do_click(locators.download_Button)
        time.sleep(6)
        pass


