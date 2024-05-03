from selenium.webdriver.common.by import By


class Locators:
    searchchronic = (By.XPATH, '//*[@id="search_input_all_addCCtable"]')
    searchbtn = (By.XPATH, '//*[@id="login"]/div[1]/div[2]/ul/li[2]/div/div/div/div/span')