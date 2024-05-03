from selenium.webdriver.common.by import By


class inactive_Locators:
  inactive_dot_btn = (By.XPATH, '//*[@id="PatientTable"]/tbody/tr[1]/td[9]/div/div/a/i')
  inactive_btn = (By.XPATH, '//*[@id="PatientTable"]/tbody/tr[1]/td[9]/div/div/div/a[2]')
  inactive_input= (By.XPATH, '//*[@id="inactiveComment"]')
  inactive_full_btn= (By.XPATH, '//*[@id="DeletePtsModal"]/div/div/div[2]/div/button')
  patient_Status_btn = (By.XPATH, '//*[@id="login-row"]/ul/li[7]/a')
  inactive_button = (By.XPATH, '//*[@id="login"]/div[1]/div[1]/div/button[2]')

