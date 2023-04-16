from selenium.webdriver.common.by import By

from pageObjectSauceDemo.OverviewPage import OverviewPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    zip_code = (By.XPATH, "//input[@id='postal-code']")
    continue_button = (By.XPATH, "//input[@id='continue']")

    def getFirstName(self):
        return self.driver.find_element(*CheckOutPage.first_name)

    def getLastName(self):
        return self.driver.find_element(*CheckOutPage.last_name)

    def getZipCode(self):
        return self.driver.find_element(*CheckOutPage.zip_code)

    def getContinueButton(self):
        self.driver.find_element(*CheckOutPage.continue_button).click()
        return OverviewPage(self.driver)
