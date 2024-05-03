import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData

from pageObject.pages.practice_Setup import do_practice_setup_Page
from pageObject.pages.locators.simple_search_chronic_condition.simple_search_chronic_condition import simple_search_locators
from pageObject.pages.loginPage import loginPage
from pageObject.config.simple_search_chronic import simple_searchChronic_Data
from pageObject.pages.simple_seach_chronic_condition import simple_search_chronic_conditions






def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)

        practice_setup = do_practice_setup_Page(driver)
        practice_setup.do_practice_setup()

        # add_ChronicCondition = do_add_ChronicCondition(driver)
        # add_ChronicCondition.do_addChronicCondition(add_chronic_condition.chronicCondition)

        simple_search_chronic_condition = simple_search_chronic_conditions(driver)
        simple_search_chronic_condition.do_simple_search(simple_searchChronic_Data.search)

        # search_ChronicConditions = do_SearchCC (driver)
        # search_ChronicConditions.do_SearchCC(search_Data.search)
        #
        #
        # # search_ChronicCondition = manage_chronic_condition(driver)
        # # search_ChronicCondition.do_SearchCC(searchCC_Data.search, searchCC_Data.edit)


        time.sleep(6)



        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

