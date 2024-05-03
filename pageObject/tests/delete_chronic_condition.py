import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData
from pageObject.config.search_Config import search_Data
from pageObject.pages.searchpage import do_Search_Page
from pageObject.pages.loginPage import loginPage
from pageObject.pages.practice_Setup import  do_practice_setup_Page
from pageObject.config.add_Chronic_condition import add_chronic_condition_Data
from pageObject.pages.addChronicConditionpage import do_add_ChronicCondition
from pageObject.config.simple_search_chronic import simple_searchChronic_Data
from pageObject.pages.simple_seach_chronic_condition import simple_search_chronic_conditions
from pageObject.pages.delete_chronic import delete_chronic_condition
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

        time.sleep(2)

        # simple_search_chronic_condition = simple_search_chronic_conditions(driver)
        # simple_search_chronic_condition.do_simple_search(simple_searchChronic_Data.search)

        time.sleep(2)

        Delete_chronic_condition = delete_chronic_condition(driver)
        #Delete_chronic_condition.do_delete_chronic_condition()

        if Delete_chronic_condition.do_delete_chronic_condition():
            print("Succesfully deleted")

        else:
            print("abc")




        time.sleep(6)



        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

