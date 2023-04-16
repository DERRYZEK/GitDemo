from selenium.webdriver.common.by import By

from pageObjectSauceDemo.CheckOutPage import CheckOutPage


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    checkout_button = (By.CSS_SELECTOR, "#checkout")

    def getCheckOutButton(self):
        self.driver.find_element(*CartPage.checkout_button).click()
        return CheckOutPage(self.driver)
