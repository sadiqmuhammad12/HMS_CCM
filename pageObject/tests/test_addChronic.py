import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData
from pageObject.config.search_Config import search_Data
from pageObject.pages.console_Page import do_Console_Page
from pageObject.pages.loginPage import loginPage
from pageObject.pages.practice_Setup import  do_practice_setup_Page
from pageObject.pages.addChronicConditionpage import do_add_ChronicCondition
from pageObject.pages.locators.add_ChronicCondition_locator.add_Chronic_Condition_locator import Locators
from pageObject.config.add_Chronic_condition import add_chronic_condition
from pageObject.config.patientConsole_Config import console_Data
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.pages.locators.searchLocator import locators




def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)

        practice_setup = do_practice_setup_Page(driver)
        practice_setup.do_practice_setup()

        add_ChronicCondition = do_add_ChronicCondition(driver)
        add_ChronicCondition.do_addChronicCondition(add_chronic_condition.chronicCondition)

        time.sleep(6)



        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

