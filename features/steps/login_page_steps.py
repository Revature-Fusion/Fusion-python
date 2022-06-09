from lib2to3.pgen2 import driver
import unittest
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.login_page import LoginPage



@given('The User or Admin are on the Login Page')
def get_to_login(context):
    driver: WebDriver = context.driver
    driver.get('file:///C:/Users/tomiw/Desktop/Work/Fusion-python/login.html')
    #this directory is local, must be changed when run on a different system


@when('The User or Admin enter their username')
def user_enters_username(context):
    login_page: LoginPage = context.login_page
    login_page.login_username().click()
    login_page.send_keys("testusername")

@when('The User or Admin enters their password')
def verify_title_login(context):
    LoginPage: LoginPage = context.login_page
    LoginPage.login_password().click()
    LoginPage.send_keys("testpassword")

@when('The User or Admin clicks on the login button')
def submit_login_form(context):
    LoginPage: LoginPage = context.login_page
    LoginPage.login_btn().click()

@then('They are able to log into the website')
def verify_login(context):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.title, "Home Page")
    #Home Page title Name must be "Home Page" for test to pass

