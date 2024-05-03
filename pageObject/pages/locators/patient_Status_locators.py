
from selenium.webdriver.common.by import By


class patient_Status_locators:
    patient_Status_btn = (By.XPATH , '//*[@id="login-row"]/ul/li[7]/a')
    # inactive_button = (By.XPATH,'//*[@id="login"]/div[1]/div[1]/div/button[2]')
    active_button = (By.XPATH,'//*[@id="login"]/div[1]/div[1]/div/button[1]')
