from selenium.webdriver.common.by import By


class simple_search_locators:
    search_bar = (By.XPATH , '//*[@id="search_input_all_addCCtable"]')
    input_data = (By.XPATH, '//*[@id="search_input_all_addCCtable"]')
    search_bar_btn = (By.XPATH, '//*[@id="login"]/div[1]/div[2]/ul/li[2]/div/div/div/div/span')