import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData

from pageObject.pages.loginPage import loginPage
from pageObject.pages.inactive_edit_Page import inactive_edit_Patient
from pageObject.config.inactive_edit_Patient import inactive_edit_Patient_Data





def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)

        inactive_Edit_Patient = inactive_edit_Patient(driver)
        inactive_Edit_Patient.do_inactive_edit_Patient(inactive_edit_Patient_Data.first_Name, inactive_edit_Patient_Data.last_Name, inactive_edit_Patient_Data.DOB, inactive_edit_Patient_Data.phone_No, inactive_edit_Patient_Data.Email,inactive_edit_Patient_Data.Ins_policy,inactive_edit_Patient_Data.Adress )

        time.sleep(6)



        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

