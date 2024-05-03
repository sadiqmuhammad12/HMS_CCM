import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.select import Select
from pageObject.config.config import testData
from pageObject.config.patient_Status_Config import patient_Status_data
from pageObject.pages.Signuppage import SignupPage
from pageObject.pages.locators.managestafflocators.manageStafflocators import Locators
from pageObject.pages.loginPage import loginPage
from pageObject.pages.patient_Status_Page import patient_Status
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators


def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()
        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)
        Patient_Status = patient_Status(driver)
        Patient_Status.do_Patient_Status_Crud()

        time.sleep(6)

        # get the current URL of the page
        current_url = driver.current_url
        # check if the expected text is in the URL

        if "otp-screen" in current_url:
            print("User is logged in and redirected to the otp-screen page")

        else:
            print("User login failed or was not redirected to the otp-screen page")

        # close the web driver instance
        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
