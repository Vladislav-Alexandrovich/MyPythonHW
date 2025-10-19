from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, browser):
        self.browser = browser

    def checkout(self):
        self.browser.find_element(By.ID, "checkout").click()

    # def __init__(self, driver):
    #     driver = webdriver.Firefox()
    #     self.driver = driver
    #     # driver.get("https://www.saucedemo.com/cart.html")