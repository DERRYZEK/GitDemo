from selenium.webdriver.common.by import By

from pageObjectSauceDemo.CartPage import CartPage


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    products_names = (By.XPATH, "//div[@class='inventory_item_name']")
    add_to_cart = (By.XPATH, "//button[contains(@class,'btn_primary')]")
    cart_button = (By.XPATH, "//a[@class='shopping_cart_link']")

    def getProducts(self):
        return self.driver.find_elements(*ProductsPage.products_names)

    def getAddCartButton(self):
        return self.driver.find_elements(*ProductsPage.add_to_cart)

    def cartButton(self):
        self.driver.find_element(*ProductsPage.cart_button).click()
        return CartPage(self.driver)
