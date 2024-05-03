import time
import chromedriver_autoinstaller

from selenium import webdriver
from pageObject.config.config import testData
from pageObject.pages.console_Page import do_Console_Page
from pageObject.pages.loginPage import loginPage
from pageObject.config.patientConsole_Config import console_Data
from pageObject.pages.carePlan_download_Page import do_carePlan_Download_page




def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)

        patient_Console = do_Console_Page(driver)
        patient_Console.do_Patientconsole(console_Data.input_Data)

        # patient_Console.do_Patientconsole(console_Data.medical_History,console_Data.surgical_History,console_Data.family_History,console_Data.medication_Allergies,console_Data.recent_Hospital_Stays,console_Data.recent_Injuries,console_Data.recent_Treatment,console_Data.medical_history_last_Q)
        care_Download = do_carePlan_Download_page(driver)
        care_Download.do_CarePlan_download()
        time.sleep(6)



        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

