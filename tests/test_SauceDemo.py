from pageObjectSauceDemo.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestSauceDemo(BaseClass):

    def test_saucedemo(self):
        log = self.getLogger()

        loginPage = LoginPage(self.driver)

        log.info("Entering user name")
        loginPage.userName().send_keys("standard_user")
        log.info("Entering password")
        loginPage.getPassword().send_keys("secret_sauce")

        log.info("Getting all products")
        productsPage = loginPage.loginButton()
        products = productsPage.getProducts()

        i = -1

        for product in products:
            i = 1 + 1
            product_name = product.text

            if product_name == "Sauce Labs Backpack":
                productsPage.getAddCartButton()[i].click()

        cartPage = productsPage.cartButton()

        checkoutPage = cartPage.getCheckOutButton()

        checkoutPage.getFirstName().send_keys("Derrick")
        checkoutPage.getLastName().send_keys("Owusu Ansah")
        checkoutPage.getZipCode().send_keys("00233")

        overviewPage = checkoutPage.getContinueButton()
        overviewPage.getFinishButton().click()

        message = overviewPage.getSuccessMessage().text

        assert "Thank you for your order!" in message

