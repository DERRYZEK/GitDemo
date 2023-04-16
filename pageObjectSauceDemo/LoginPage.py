from selenium.webdriver.common.by import By

from pageObjectSauceDemo.ProductsPage import ProductsPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    user_name = (By.CSS_SELECTOR, "input[id='user-name']")
    password = (By.CSS_SELECTOR, "input[id='password']")
    login_button = (By.CSS_SELECTOR, "input[id = 'login-button']")

    def userName(self):
        return self.driver.find_element(*LoginPage.user_name)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def loginButton(self):
        self.driver.find_element(*LoginPage.login_button).click()
        return ProductsPage(self.driver)

