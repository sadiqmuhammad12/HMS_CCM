from selenium.webdriver.common.by import By


class Locators:
  addChronicConditionbtn = (By.XPATH, '//*[@id="login"]/div[1]/div[2]/ul/li[1]/div/div/a')
  chronicCondition = (By.XPATH,'//*[@id="ChronicConditionName"]')
  savebtn = (By.XPATH,'//*[@id="addAlonccForm"]/div[2]/div/a')