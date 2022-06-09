from atexit import register
import unittest
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.register_page import RegisterPage


@given('The User is on register page')
def create_account(context):
    driver: WebDriver = context.driver
    driver.get("file:///C:/Users/tomiw/Desktop/Work/Fusion-python/registration.html")
    #this directory is local, must be changed when run on a different system

# @when('They navigate to the register form')
# def nav_to_form(context):

#     pass

@when('They enter their Role, Email, First Name, Last Name, Username, Password')
def enter_user_info(context):
    register_page: RegisterPage = context.register_page
    register_page.role()
    register_page.user_email().click()
    register_page.send_keys("mattsmith@electronicmail.com")
    register_page.user_first_name().click()
    register_page.send_keys("matt")
    register_page.user_last_name
    register_page.send_keys("smith")
    register_page.user_username
    register_page.send_keys("matts123")
    register_page.user_password
    register_page.send_keys("123456789")

@when('They click the Register button')
def submit_register(context):
    register_page: RegisterPage = context.register_page
    register_page.register_btn().click()

@then('The form is submitted and they are able to login')
def verify_title_change(context):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.title, "Registration Page")


@given('The Guest is on the register page')
def save_account(context):
    driver: WebDriver = context.driver
    driver.get("file:///C:/Users/tomiw/Desktop/Work/Fusion-python/registration.html")
    #this directory is local, must be changed when run on a different system

#@when('They navigate to the guest form')
#def nav_to_guest_form(context):
#    pass

@when('They enter their Email, First Name, Last Name')
def guest_info(context):
    guest_page : RegisterPage = context.guest_page
    guest_page.guest_email().click()
    guest_page.send_keys("jonsnow@electronicmail.com")
    guest_page.guest_first_name().click()
    guest_page.send_keys("jon")
    guest_page.guest_last_name().click()
    guest_page.send_keys("snow")

@when('They click on the Submit button')
def submit_guest(context):
    guest_page: RegisterPage = context.guest_page
    guest_page.guest_btn().click()

@then('The information is saved for them')
def guest_saved(context):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.title, "Login")
    #Home Page title Name must be "Home Page" for test to pass
