import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData
from pageObject.pages.un_Assigned_page import unassignedPage
from pageObject.pages.loginPage import loginPage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.config.signup_config import signup_testData




def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)

        Unassigned_Page = unassignedPage(driver)
        Unassigned_Page.do_unassignedPatient()

        time.sleep(6)

        # get the current URL of the page
        current_url = driver.current_url
        # check if the expected text is in the URL

        # close the web driver instance
        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

