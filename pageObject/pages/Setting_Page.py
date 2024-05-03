from pageObject.pages.basePage import basePage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.pages.locators.Setting.Setting import Locators
from pageObject.pages.locators.Console_locators.Console_locators import locators
from pageObject.config.search_Config import search_Data


class setting_Page(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(searchpage.base_url)

    def do_Setting(self,current_pass,new_Pass,confirm_Pass):

        self.do_click(Locators.setting_btn)
        self.do_click(Locators.change_Pass)
        self.do_send_keys(Locators.current_pass,current_pass)
        self.do_send_keys(Locators.new_Pass, new_Pass)
        self.do_send_keys(Locators.confirm_Pass,confirm_Pass)
        self.do_click(Locators.sav_Btn)





