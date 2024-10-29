from behave import given, when, then
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from selenium import webdriver
import time


@given('I am on the signup page')
def step_impl(context):
    context.driver.get("https://magento.softwaretestingboard.com/customer/account/create/")

@when('I enter valid information in all required fields')
def step_impl(context):
    context.signup_page.enter_first_name("Test_Prajjwal")
    context.signup_page.enter_last_name("User_prajjwal")
    context.signup_page.enter_email("testuser@_prajjwalexample.com")
    context.signup_page.enter_password("sandili@123")
    context.signup_page.enter_confirm_password("sandili@123")

@when('I submit the signup form')
def step_impl(context):
    context.signup_page.click_signup()
    time.sleep(3)

@then('I should be redirected to the account dashboard')
def step_impl(context):
    assert "dashboard" in context.driver.current_url

@then('I should see a confirmation message for account creation')
def step_impl(context):
    assert "Thank you for registering" in context.driver.page_source


@given('I am on the login page')
def step_impl(context):
    context.driver.get("https://magento.softwaretestingboard.com/customer/account/login/")

@when('I enter valid login credentials')
def step_impl(context):
    context.login_page.enter_email("testuser@example.com")
    context.login_page.enter_password("Password123")

@when('I submit the login form')
def step_impl(context):
    context.login_page.click_login()
    time.sleep(3)

@then('I should see an error message indicating invalid credentials')
def step_impl(context):
    assert "Invalid login or password" in context.driver.page_source

@given('I have an existing account')
def step_impl(context):
    print("Assuming the user has an existing account.")

@when('I enter an invalid username or password')
def step_impl(context):
    context.login_page.enter_email("invaliduser@example.com")
    context.login_page.enter_password("wrongpassword")
