from selenium import webdriver
from pages.signup_page import SignupPage
from pages.login_page import LoginPage

def before_scenario(context, scenario):
    # Initialize the WebDriver
    context.driver = webdriver.Chrome()  # Adjust if using a different browser
    context.driver.maximize_window()
    
    # Initialize page objects
    context.signup_page = SignupPage(context.driver)
    context.login_page = LoginPage(context.driver)

def after_scenario(context, scenario):
    # Quit the WebDriver
    context.driver.quit()
