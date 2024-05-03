from selenium.webdriver.common.by import By


class Locators:
 setting_btn =(By.XPATH, '//*[@id="collapsibleNavId"]/form/a[1]/i')
 change_Pass = (By.XPATH,'//*[@id="login"]/div[2]/div/div/div[2]/div/div/div/p/a')
 current_pass = (By.XPATH,'//*[@id="oldpass"]')
 new_Pass = (By.XPATH,'//*[@id="newpassword"]')
 confirm_Pass = (By.XPATH,'//*[@id="confirmpassword"]')
 sav_Btn = (By.XPATH,'//*[@id="resetpassword"]/div/div[4]/a')