from selenium.webdriver.common.by import By


class signup_locators:
    signupbtn = (By.CLASS_NAME,'text-purple.ahover.text-center')
    PracticeName = (By.ID, 'practicename')
    PracticeAddress1 = (By.ID, 'practiceaddress1')
    PracticeAddress2 = (By.ID, 'practiceaddress2')
    Country = (By.ID, 'Country')
    City = (By.ID, 'city')

    SelectState = (By.CLASS_NAME, 'filter-option-inner-inner')
    state_value = (By.XPATH, '//*[@id="pracReg"]/div[2]/div[3]/div/div/div/div[2]/ul/li[3]/a/span')
    Zip = (By.ID, 'Zip')
    SelectDesignation = (By.ID, 'doc_designation')
    ProviderFirstName = (By.ID, 'providerfirstname')
    ProviderLastName = (By.ID, 'providerlastname')
    UserName = (By.ID, 'username')
    Email = (By.ID, 'email')
    AlertMail = (By.ID, 'AlertEmail')
    PhoneNumber = (By.ID, 'contactno')
    password = (By.ID, 'Pass')
    ConfirmPass = (By.ID, 'Cpass')
    checkbox = (By.ID,'TC')
    captcha = (By.CLASS_NAME,'recaptcha-checkbox-border')
    submitbtn = (By.CLASS_NAME,'btn.custom-btn.mt-2')
