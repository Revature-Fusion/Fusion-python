import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def before_all(context):

    driver: WebDriver = webdriver.Chrome('C:/Users/Admin/Desktop/Project 1/chromedriver.exe')




def after_all(context):
    context.driver.quit()
    print("ended")