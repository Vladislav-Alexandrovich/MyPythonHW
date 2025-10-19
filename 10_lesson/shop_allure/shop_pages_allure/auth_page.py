"""
Этот класс содержит функции заполнения полей авторизации интернет-магазина,
переменные передаются из файла теста
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class AuthPage:
    @allure.feature("CREATE")
    @allure.step("Создание драйвера {browser}")
    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser


    @allure.feature("INPUT")
    @allure.step("Ввод данных для логинизациии логин {term1}"
                 "пароль {term2}")
    def fill_login_fields(self, term1: str, term2: str) -> None:
        self.browser.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(term1)
        self.browser.find_element(
            By.CSS_SELECTOR, "#password").send_keys(term2)
        self.browser.find_element(
            By.CSS_SELECTOR, "#login-button").click()
