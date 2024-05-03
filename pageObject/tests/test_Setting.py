import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData
from pageObject.pages.loginPage import loginPage
from pageObject.pages.Setting_Page import setting_Page
from pageObject.config.Setting import setting_Data





def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)

        Setting_Page = setting_Page(driver)
        Setting_Page.do_Setting(setting_Data.current_Pass,setting_Data.new_Pass,setting_Data.confirm_Pass)



        time.sleep(6)



        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

