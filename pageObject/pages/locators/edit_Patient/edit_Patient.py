from selenium.webdriver.common.by import By


class Locators:
  edit_Pdots_btn = (By.XPATH, '//*[@id="PatientTable"]/tbody/tr[1]/td[9]/div/div/a/i')
  edit_Patient_btn = (By.XPATH, '//*[@id="PatientTable"]/tbody/tr[1]/td[9]/div/div/div/a[1]')
  first_Name = (By.XPATH, '//*[@id="editPtsFName"]')
  last_Name = (By.XPATH, '//*[@id="editPtsLName"]')
  DOB = (By.XPATH, '//*[@id="editPtsDate"]')
  Gender = (By.XPATH, '//*[@id="editPtsGender"]')
  gender_Value =(By.XPATH,'//*[@id="editPtsGender"]/option[1]')
  phone_No = (By.XPATH, '//*[@id="editPtsPhone"]')
  Email = (By.XPATH,'//*[@id="editPtsEmail"]')
  Language = (By.XPATH,'//*[@id="editptsLanguages"]')
  language_Vlaue = (By.XPATH, '//*[@id="editptsLanguages"]/option[2]')
  Insurance = (By.XPATH,'//*[@id="editPtsIns"]')
  insurance_Value = (By.XPATH,'//*[@id="editPtsIns"]/option[4]')
  ins_Policy = (By.XPATH,'//*[@id="editPtsInsPno"]')
  Adress = (By.XPATH,'//*[@id="editPtsAddress"]')
  Update_btn = (By.XPATH, '//*[@id="PtsEnro1"]/div[4]/div/ul/li/a')