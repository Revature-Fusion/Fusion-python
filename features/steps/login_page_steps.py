import unittest
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.login_page import LoginPage


@given('The User or Admin are on the Login Page')
def get_to_login(context):
    pass


@when('The User or Admin enter their username')
def user_enters_username(context):
    pass


@when('The User or Admin enters their password')
def verify_title_login(context):
    pass

@when('The User or Admin clicks on the login button')
def submit_login_form(context):
    pass

@then('They are able to log into the website')
def verify_login(context):
    pass

