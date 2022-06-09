import unittest
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.register_page import RegisterPage


@given('The User is on register page')
def create_account(context):
    pass

@when('They navigate to the register form')
def nav_to_form(context):
    pass

@when('They enter their Role, Email, First Name, Last Name, Username, Password')
def enter_user_info(context):
    pass

@when('They click the Register button')
def submit_register(context):
    pass

@then('The form is submitted and they are able to login')
def verify_title_change(context):
    pass


@given('The Guest is on the register page')
def save_account(context):
    pass

@when('They navigate to the guest form')
def nav_to_guest_form(context):
    pass

@when('They enter their Email, First Name, Last Name')
def guest_info(context):
    pass

@when('They click on the Submit button')
def submit_guest(context):
    pass

@then('The information is saved for them')
def guest_saved(context):
    pass
