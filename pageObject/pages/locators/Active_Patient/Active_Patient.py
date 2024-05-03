from selenium.webdriver.common.by import By


class active_Locators:
  Active_Dash_btn = (By.XPATH, '//*[@id="login"]/div[1]/div[2]/ul/li[1]/ul/li[2]/label')
  Active_Dot_btn = (By.XPATH, '//*[@id="PatientTable"]/tbody/tr[1]/td[9]/div/div/a/i')
  Active_btn = (By.XPATH, '//*[@id="PatientTable"]/tbody/tr[1]/td[9]/div/div/div/a[2]')
  Active_input= (By.XPATH, '//*[@id="activeComment"]')
  Active_full_btn= (By.XPATH, '//*[@id="ActivePtsModal"]/div/div/div[2]/div/button')
  patient_Status_butn = (By.XPATH , '//*[@id="login-row"]/ul/li[7]/a')
  Active_buutton = (By.XPATH,'//*[@id="login"]/div[1]/div[1]/div/button[1]')
