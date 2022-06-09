import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.login_page import LoginPage
from features.pages.register_page import RegisterPage

ser= Service()
driver: WebDriver= webdriver.Chrome(service=ser)
login= LoginPage(driver)
register= RegisterPage(driver)

def _test():
    try:
        driver.get("file:///C:/Users/tomiw/Desktop/Work/Fusion-python/login.html")
        #change directory for local system^
        time.sleep(3)
        login.login_username.send_keys("sampleusername")
        login.login_password.send_keys("samplepassword")
        login.login_btn().click()
        time.sleep(3)
        driver.get("file:///C:/Users/tomiw/Desktop/Work/Fusion-python/registration.html")
        #change directory for local system^
        register.role()
        register.user_email().send_keys("mattsmith@electronicmail.com")
        register.user_first_name().send_keys("matt")
        register.user_last_name().send_keys("smith")
        register.user_username().send_keys("matts123")
        register.user_password().send_keys("123456789")
        register.register_btn().click()
        time.sleep(3)
        register.guest_email().send_keys("jonsnow@electronicmail.com")
        register.guest_first_name().send_keys("jon")
        register.guest_last_name().send_keys("snow")
        register.guest_btn().click()
        time.sleep(3)
        assert "successfully registered user" == driver.switch_to.alert.text
    except AssertionError:
        print(f"could not register user:{driver.switch_to.alert.text}")
    else:
        ("user registered")
    finally:
        driver.quit()