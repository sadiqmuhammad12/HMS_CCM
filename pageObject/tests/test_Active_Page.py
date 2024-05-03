import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData

from pageObject.pages.loginPage import loginPage
from pageObject.pages.Active_Page import Active_Patient
from pageObject.config.Active_Patient_Config import Active_Data
from pageObject.pages.patient_Status_Page import patient_Status
from pageObject.pages.locators.patient_Status_locators import patient_Status_locators






def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)

        Active_Patients = Active_Patient(driver)
        Active_Patients.do_Active_Patient(Active_Data.Active_Comment)

        patient_status = patient_Status(driver)
        patient_status.do_Patient_Status()

        time.sleep(6)



        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

