from selenium.webdriver.common.by import By
import time

class locators:
  billing_Report_Btn = (By.XPATH,'//*[@id="login-row"]/ul/li[6]/a')
  select_Clinician = (By.XPATH,'//*[@id="precClinicion"]')
  selected_Value = (By.XPATH,'//*[@id="precClinicion"]/option[2]')
  from_Value = (By.XPATH,'//*[@id="billFrom"]')
  to_Value = (By.XPATH,'//*[@id="billTo"]')
  downloadbtn = (By.XPATH,'//*[@id="billingBtn"]/img')