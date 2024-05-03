from selenium.webdriver.common.by import By


class Locators:
  edit_dots_btn = (By.XPATH, '//*[@id="login-row"]/ul/li[1]/div/div/a/i')
  edit_OwnerP_btn = (By.XPATH, '//*[@id="login-row"]/ul/li[1]/div/div/div/a')
  first_Name = (By.ID, 'UpFname')
  last_Name = (By.ID, 'UpLname')
  user_Name = (By.ID, 'UpUname')
  alert_Mail = (By.ID, 'UpAlertEmail')
  phone_No = (By.ID, 'UpNumber')
  Adress = (By.ID,'UpAddress')
  City = (By.ID,'UpCity')
  select_state = (By.XPATH,'//*[@id="UpdateProfileModal"]/div/div/div[2]/form/div[4]/div[1]/div/button/div')
  value_select_state = (By.XPATH,'//*[@id="UpdateProfileModal"]/div/div/div[2]/form/div[4]/div[1]/div/div/div[2]/ul/li[2]/a/span')
  zip = (By.ID,'UpZip')
  save_btn = (By.XPATH, '//*[@id="UpdateProfileModal"]/div/div/div[2]/div/div/button')