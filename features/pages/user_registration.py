from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class UserRegisterPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def email(self):
        return self.driver.find_element(by=By.ID, value="email")

    def first_name(self):
        return self.driver.find_element(by=By.ID, value="fistName")

    def last_name(self):
        return self.driver.find_element(by=By.ID, value="lastName")

    def username(self):
        return self.driver.find_element(by=By.ID, value="username")

    def password(self):
        return self.driver.find_element(by=By.ID, value="password")

    def role(self):
        return self.driver.find_element(by=By.ID, value="role")

    def submit_button(self):
        return self.driver.find_element(by=By.ID, value="btn")