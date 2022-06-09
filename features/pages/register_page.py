from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class RegisterPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def role(self):
        dropdown = self.driver.find_element(by=By.ID, value="roleList")
        return dropdown.select_by_value("MEMBER")

    def user_email(self):
        return self.driver.find_element_by_xpath("//div[@id='inner1']//*[@id='email']")

    def user_first_name(self):
        return self.driver.find_element(by=By.ID, value="firstName")

    def user_last_name(self):
        return self.driver.find_element(by=By.ID, value="lastName")

    def user_username(self):
        return self.driver.find_element(by=By.ID, value="username")

    def user_password(self):
        return self.driver.find_element(by=By.ID, value="password")

    def guest_email(self):
        return self.driver.find_element(by=By.ID, value="guestemail")

    def guest_first_name(self):
        return self.driver.find_element(by=By.ID, value="guestfirstName")

    def guest_last_name(self):
        return self.driver.find_element(by=By.ID, value="guestlastName")
