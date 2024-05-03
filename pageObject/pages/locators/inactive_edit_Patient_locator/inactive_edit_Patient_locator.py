from selenium.webdriver.common.by import By
import time


class inactive_edit_Locators:
  Inactive_dash_btn = (By.XPATH,'//*[@id="login"]/div[1]/div[2]/ul/li[1]/ul/li[2]/label')
  inactive_edit_dot_btn = (By.XPATH, '//*[@id="PatientTable"]/tbody/tr[1]/td[9]/div/div/a/i')
  inactive_edit_btn = (By.XPATH, '//*[@id="PatientTable"]/tbody/tr[1]/td[9]/div/div/div/a[1]')
  first_Name = (By.ID,'editPtsFName')
  last_Name = (By.ID, 'editPtsLName')
  DOB = (By.XPATH,'//*[@id="editPtsDate"]')
  time.sleep(3)
  Gender = (By.XPATH,'//*[@id="editPtsGender"]')
  Gender_Value = (By.XPATH,'//*[@id="editPtsGender"]/option[2]')
  phone_No = (By.XPATH,'//*[@id="editPtsPhone"]')
  email = (By.ID , 'editPtsEmail')
  Language = (By.XPATH,'//*[@id="editptsLanguages"]')
  Language_Vlaue = (By.XPATH,'//*[@id="editptsLanguages"]/option[2]')
  Insurance = (By.XPATH,'//*[@id="editPtsIns"]')
  Insurance_Vlaue =(By.XPATH,'//*[@id="editPtsIns"]/option[2]')
  insurance_policy = (By.ID,'editPtsInsPno')
  Adress = (By.ID,'editPtsAddress')
  update_btn = (By.XPATH,'//*[@id="PtsEnro1"]/div[4]/div/ul/li/a')


