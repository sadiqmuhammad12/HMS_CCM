import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData
from pageObject.pages.loginPage import loginPage
from pageObject.pages.patient_Crud_Page import patient_Status_Crud



def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()
        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)
        Patient_Status_Crud = patient_Status_Crud(driver)
        Patient_Status_Crud.do_Patient_Status_Crud()

        driver.quit()
    except Exception as e:
        print("An error occurred:", e)

    if __name__ == "__main__":
        main()




