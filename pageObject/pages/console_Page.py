from lib2to3.pgen2 import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
from pageObject.pages.basePage import basePage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.pages.locators.Console_locators.Console_locators import locators
from pageObject.config.search_Config import search_Data


class do_Console_Page(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(console_Data.base_url)

    def do_Patientconsole(self,input_Yes):
        self.do_click(locators.patientBtn)
        time.sleep(3)
        # self.do_click(locators.annual_Welness)
        # self.do_click(locators.plus_btn)
        # self.do_send_keys(locators.medical_History,medical_history)
        # self.do_send_keys(locators.surgical_History, surgical_History)
        # self.do_send_keys(locators.family_History,family_History)
        # self.do_send_keys(locators.medication_Allergies, medication_Allergies)
        # self.do_send_keys(locators.recent_Hospital_Stay, recent_Hospital_Stays)
        # self.do_send_keys(locators.recent_Injuries, recent_injuries)
        # self.do_send_keys(locators.recent_Treatments, recent_Treatments)
        # self.do_send_keys(locators.medical_history_last_Q, medical_history_last_Q)
        # self.do_click(locators.save_btn_annual)
        # self.do_click(locators.carePlanbtn)
        # self.do_click(locators.start_btn)
        time.sleep(3)
        # self.do_click(locators.plus_careplan_btn)
        # self.do_click(locators.cognitive_btn1)
        # self.do_click(locators.cognitive_btn1_yes)
        # self.do_send_keys(locators.cognitive_input_yes,input_Yes)
        # self.do_click(locators.cognitive_btn2)
        # self.do_click(locators.cognitive_btn3)
        # self.do_click(locators.cognitive_btn4)
        # self.do_click(locators.cognitive_btn5)
        # time.sleep(3)
        # self.do_click(locators.cognitive_save_btn)
        # self.do_click(locators.psychosocial_plus_btn)
        # self.do_click(locators.psychosocial_btn1)
        # self.do_click(locators.psychosocial_btn2)
        # self.do_click(locators.psychosocial_btn3)
        # self.do_click(locators.psychosocial_btn4)
        # self.do_click(locators.psychosocial_btn5)
        # self.do_click(locators.psychosocial_btn6)
        # time.sleep((3))
        # self.do_click(locators.psychosocial_btn7)
        # self.do_click(locators.psychosocial_btn8)
        # self.do_click(locators.psychosocial_btn9)
        # self.do_click(locators.psychosocial_btn10)
        # time.sleep((3))
        # self.do_click(locators.psychosocial_btn11)
        # self.do_click(locators.psychosocial_btn12)
        # self.do_click(locators.psychosocial_save_btn13)


