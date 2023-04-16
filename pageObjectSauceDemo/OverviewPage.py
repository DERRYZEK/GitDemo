from selenium.webdriver.common.by import By


class OverviewPage:
    def __init__(self, driver):
        self.driver = driver

    finish_button = (By.XPATH, "//button[@id='finish']")
    success_message = (By.CSS_SELECTOR,".complete-header")

    def getFinishButton(self):
        return self.driver.find_element(*OverviewPage.finish_button)

    def getSuccessMessage(self):
        return self.driver.find_element(*OverviewPage.success_message)
