from selenium.webdriver.common.by import By


class Locators:
    searchCC =(By.XPATH, '//*[@id="search_input_all_addCCtable"]')
    searchCCbtn = (By.XPATH, '//*[@id="login"]/div[1]/div[2]/ul/li[2]/div/div/div/div/span')
    # deletebtn =(By.XPATH,'//*[@id="addCCtable"]/tbody/tr[2]/td[3]/div/div[2]/a/span')
    # deletebtn2 = (By.XPATH, '//*[@id="DeleteCC"]/div/div/div[2]/div/button')
    editbtn = (By.XPATH, '//*[@id="addCCtable"]/tbody/tr[1]/td[3]/div/div[1]/a/span')
    # editCC = (By.XPATH, '//*[@id="editCCname"]')
    editinput = (By.ID, "editCCname")
    savebtn = (By.XPATH, '//*[@id="editAloneCCModal"]/div/div/div[2]/form/div[2]/div/a')
    deleteChronicConditionbtn = (By.XPATH, '//*[@id="addCCtable"]/tbody/tr[1]/td[3]/div/div[2]/a/span')
    deletefull = (By.XPATH, ' deletechroniccondition =(By)')

