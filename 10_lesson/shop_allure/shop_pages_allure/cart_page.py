"""
Этот класс содержит функцию перехода в корзину интернет-магазина
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class CartPage:
    @allure.feature("CREATE")
    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser

    @allure.feature("SELECT")
    @allure.step("Переход в корзину")
    def checkout(self) -> None:
        self.browser.find_element(By.ID, "checkout").click()
