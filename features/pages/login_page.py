from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_username(self):
        return self.driver.find_element(by=By.ID, value="username")

    def login_password(self):
        return self.driver.find_element(by=By.ID, value="password")

    def login_btn(self):
        return self.driver.find_element(by=By.ID, value="login")

