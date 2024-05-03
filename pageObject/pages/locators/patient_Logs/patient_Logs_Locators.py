from selenium.webdriver.common.by import By


class Locators:
  patient_Logs_btn = (By.XPATH, '//*[@id="login-row"]/ul/li[10]/a')
  edit = (By.XPATH,'//*[@id="btnEdit"]/span')
  description = (By.XPATH,'//*[@id="destimelog"]')
  save_bttn = (By.XPATH, '//*[@id="timelogsubmit"]')

