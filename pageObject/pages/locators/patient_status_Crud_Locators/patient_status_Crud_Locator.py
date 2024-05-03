from selenium.webdriver.common.by import By


class locators:
    patient_status_btn =(By.XPATH,'//*[@id="login-row"]/ul/li[7]/a')
    inactive_Btn =(By.XPATH,'//*[@id="login"]/div[1]/div[1]/div/button[2]')
    delete_Btn = (By.XPATH,'//*[@id="addPatientStatustable"]/tbody/tr[1]/td[6]/div/div[2]/a/span')
    delete_full_Btn = (By.XPATH,'//*[@id="DeletePatientStatus"]/div/div/div[2]/div/button')


    # login_btn_confirm_page = (By.XPATH, "//form[@id='hs-login']//i18n-string[.='Log in']")

