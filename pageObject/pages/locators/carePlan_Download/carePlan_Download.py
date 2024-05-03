from selenium.webdriver.common.by import By
import time

class locators:
    patientBtn = (By.XPATH,'//*[@id="PatientTable"]/tbody/tr[3]/td[1]/div')
    download_Button = (By.XPATH,'//*[@id="careplanchecklogo"]/td[4]')