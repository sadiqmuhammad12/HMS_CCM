import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData

from pageObject.pages.loginPage import loginPage
from pageObject.pages.inactive_Patient_page import inactive_Patient
from pageObject.config.inactive_Patient import inactive_Patient_Data
from pageObject.pages.patient_Status_Page import patient_Status






def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)

        inactive_Patients = inactive_Patient(driver)
        inactive_Patients.do_inactive_Patient(inactive_Patient_Data.inactive_input)

        time.sleep(6)
        Patient_Status = patient_Status(driver)
        Patient_Status.do_Patient_Status()



        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

