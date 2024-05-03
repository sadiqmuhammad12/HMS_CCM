import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData

from pageObject.pages.loginPage import loginPage
from pageObject.pages.edit_Patient_Page import edit_Patient
from pageObject.config.edit_Patient import edit_Patient_Data





def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)

        Edit_Patient = edit_Patient(driver)
        Edit_Patient.do_edit_Patient(edit_Patient_Data.first_Name, edit_Patient_Data.last_Name, edit_Patient_Data.DOB, edit_Patient_Data.phone_No, edit_Patient_Data.Email,edit_Patient_Data.Ins_policy,edit_Patient_Data.Adress )

        time.sleep(6)



        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

