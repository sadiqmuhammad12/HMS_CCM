import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.config import testData
from pageObject.pages.loginPage import loginPage
from pageObject.pages.billing_Report_Page import billig_Report_age
from pageObject.config.download_Billing_Report import download_Billing_Data


def main():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.useremail, testData.password)

        billing_Report = billig_Report_age(driver)
        billing_Report.do_billig_Report(download_Billing_Data.from_Value, download_Billing_Data.to_Value)
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
