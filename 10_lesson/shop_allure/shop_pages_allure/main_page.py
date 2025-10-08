"""
Этот класс содержит функцию помещения тестовых товаров
в корзину интернет-магазина
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class MainPage:
    @allure.feature("CREATE")
    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser

    @allure.feature("INPUT")
    @allure.step("Помещение товаров в корзину")
    def put_in_cart(self) -> None:
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.browser.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link").click()
