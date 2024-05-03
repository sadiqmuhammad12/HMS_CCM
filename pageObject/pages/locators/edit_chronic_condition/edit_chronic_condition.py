from selenium.webdriver.common.by import By


class Locators:
  editChronicConditionbtn = (By.XPATH, '//*[@id="addCCtable"]/tbody/tr[1]/td[3]/div/div[1]/a')
  edit_input_field = (By.XPATH, '//*[@id="editCCname"]')
  save_btn = (By.XPATH, '//*[@id="editAloneCCModal"]/div/div/div[2]/form/div[2]/div/a')