import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData
from pageObject.pages.Signuppage import SignupPage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.config.signup_config import signup_testData




def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        Signup_page = SignupPage(driver)
        Signup_page.do_Signup(signup_testData.practicename, signup_testData.practiceaddress1, signup_testData.practiceaddress2, signup_testData.Country, signup_testData.city, signup_testData.zip,signup_testData.providerfirstname, signup_testData.providerlastname, signup_testData.username, signup_testData.email, signup_testData.AlertEmail, signup_testData.contactno, signup_testData.Pass, signup_testData.Cpass)

        time.sleep(6)

        # get the current URL of the page
        current_url = driver.current_url
        # check if the expected text is in the URL
        if "net" in current_url:
            print("User is logged in and redirected to the log in page")

        else:
            print("User login failed or was not redirected to the log in page")

        # close the web driver instance
        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

