from selenium.webdriver.common.by import By

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        # Define element locators
        self.first_name_input = (By.ID, 'firstname')
        self.last_name_input = (By.ID, 'lastname')
        self.email_input = (By.ID, 'email_address')
        self.password_input = (By.ID, 'password')
        self.confirm_password_input = (By.ID, 'password-confirmation')
        self.signup_button = (By.XPATH, "//button[@title='Create an Account']")

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)

    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()
