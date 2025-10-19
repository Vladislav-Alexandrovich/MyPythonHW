from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def put_in_cart(self):
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.browser.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link").click()

# def __init__(self, driver):
#         # driver = webdriver.Firefox()
#         self.driver = driver
#         # driver.get("https://www.saucedemo.com/inventory.html")