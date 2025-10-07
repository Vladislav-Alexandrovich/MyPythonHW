import allure
from selenium.webdriver.common.by import By


class CartPage:
    @allure.feature("CREATE")
    def __init__(self, browser):
        self.browser = browser

    @allure.feature("SELECT")
    @allure.step("Переход в корзину")
    def checkout(self):
        self.browser.find_element(By.ID, "checkout").click()

    # def __init__(self, driver):
    #     driver = webdriver.Firefox()
    #     self.driver = driver
    #     # driver.get("https://www.saucedemo.com/cart.html")
