import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData
from pageObject.pages.loginPage import loginPage
from pageObject.pages.edit_Owner_provider import edit_Owner_Provider
from pageObject.config.edit_Owner_Provider import edit_Owner_Provider_Data
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators




def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)

        edit_owner = edit_Owner_Provider(driver)
        edit_owner.do_edit_Owner_Provider(edit_Owner_Provider_Data.first_Name, edit_Owner_Provider_Data.last_Name, edit_Owner_Provider_Data.user_Name, edit_Owner_Provider_Data.alert_Mail, edit_Owner_Provider_Data.phone_No, edit_Owner_Provider_Data.adress, edit_Owner_Provider_Data.city, edit_Owner_Provider_Data.select_state)

        time.sleep(6)

        # get the current URL of the page
        # current_url = driver.current_url
        # check if the expected text is in the URL


        # close the web driver instance
        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

