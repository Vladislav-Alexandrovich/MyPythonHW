from selenium.webdriver.common.by import By


class OrderPage:
    def __init__(self, browser):
        self.browser = browser

    def fill_order_details(self, term1, term2, term3):
        self.browser.find_element(By.CSS_SELECTOR, "#first-name").send_keys(term1)
        self.browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys(term2)
        self.browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(term3)
        self.browser.find_element(By.CSS_SELECTOR, "#continue").click()

    def get_total_price(self):
        total_price = self.browser.find_element(By.CSS_SELECTOR, "[data-test='total-label']").text

        return total_price

    # def __init__(self, driver):
    #     driver = webdriver.Firefox()
    #     self.driver = driver
    #     # driver.get("https://www.saucedemo.com/checkout-step-one.html")

