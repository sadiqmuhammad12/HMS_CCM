from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Locators:
    # Define locators for elements

    manage_staff_btn = (By.CLASS_NAME, 'text-reset')
    add_staff_btn = (By.XPATH, '//*[@id="login"]/div[1]/div[2]/ul/li[2]/div/div/a')

    clinician_first_name = (By.ID, 'ccfirstname')
    clinician_last_name = (By.ID, 'cclastname')
    clinician_username = (By.ID, 'ccUsername')
    clinician_password = (By.ID, 'ccPass')
    clinician_confirm_password = (By.ID, 'ccCpass')
    clinician_email = (By.ID, 'ccEmail')
    clinician_alert_mail = (By.ID, 'ccAlertEmail')
    clinician_phone_number = (By.ID, 'ccContactno')
    select_role = (By.ID, 'clinicianRole')
    clinician_city = (By.ID, 'cccity')
    select_state = (By.ID, 'ccstate')
    clinician_zip_first = (By.ID, 'ccZip')




