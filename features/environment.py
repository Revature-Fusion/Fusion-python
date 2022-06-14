import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.login_page import LoginPage
from features.pages.register_page import RegisterPage


def before_all(context):
    driver: WebDriver = webdriver.Chrome('/User/naomiscott/desktop/Revature/chromedriver')

    login_page = LoginPage(driver)
    register_page = RegisterPage(driver)

    test = unittest.TestCase()

    context.driver = driver
    context._login = login_page
    context.register_home = register_page
    context.unittest = test
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
