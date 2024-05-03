import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData
from pageObject.config.add_Patient import add_PatientData
from pageObject.pages.addPatientpage import addPatientPage
from pageObject.pages.loginPage import loginPage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators




def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()
        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)
        add_Patient = addPatientPage(driver)
        add_Patient.do_addPatient(add_PatientData.firstName, add_PatientData.lastName,add_PatientData.phone, add_PatientData.Email,add_PatientData.Address)

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

