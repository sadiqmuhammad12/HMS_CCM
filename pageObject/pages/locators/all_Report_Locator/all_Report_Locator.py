from selenium.webdriver.common.by import By
import time

class locators:
    patientBtn = (By.XPATH,'//*[@id="PatientTable"]/tbody/tr[3]/td[1]/div')
    all_Report_btn= (By.XPATH,'//*[@id="login-row"]/ul/li[11]/a')
    all_Report_Download_btn = (By.XPATH,'//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr[1]/td[3]/a/div/span/div/a/span')