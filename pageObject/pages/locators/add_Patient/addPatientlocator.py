from selenium.webdriver.common.by import By


class locators:
    loginbtn =(By.XPATH, '//*[@id="login"]/div[1]/div[2]/ul/li[2]/div/div/a')
    firstName =(By.ID, 'ptsName1')
    lastName = (By.ID, 'ptsName2')
    DOB = (By.XPATH, '//*[@id="ptsDob"]')
    Gender = (By.XPATH, '//*[@id="ptsGender"]')
    patientName = (By.ID, 'ptsPhone')
    patientEmail = (By.ID, 'ptsEmail')
    patientLanguage = (By.ID, 'ptsLanguages')
    patientInsurance = (By.ID, 'ptsInsurance')
    insurancepolicy = (By.ID, 'insPolicyno')
    Address = (By.XPATH, '//*[@id="ptsAddress"]')
    submitbtn = (By.XPATH, '//*[@id="enroll"]')

    