"""
Этот класс содержит функции оформления заказа интернет-магазина,
переменные передаются из файла теста
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class OrderPage:
    @allure.feature("CREATE")
    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser

    @allure.feature("INPUT")
    @allure.step("Заполнение данных для заказа"
                 "Имя: {term1}"
                 "Фамилия:{term2},"
                 "Индекс {term3}")
    def fill_order_details(self, term1: str, term2: str, term3: int) -> None:
        self.browser.find_element(By.CSS_SELECTOR,
                                  "#first-name").send_keys(term1)
        self.browser.find_element(By.CSS_SELECTOR,
                                  "#last-name").send_keys(term2)
        self.browser.find_element(By.CSS_SELECTOR,
                                  "#postal-code").send_keys(term3)
        self.browser.find_element(By.CSS_SELECTOR,
                                  "#continue").click()


    @allure.feature("GET")
    @allure.step("Получение суммы заказа")
    def get_total_price(self) -> float:
        value = self.browser.find_element(By.CSS_SELECTOR,
                                          "[data-test='total-label']").text
        # price = value.split(": $")[1]
        total_price = float(value.split(": $")[1])
        return total_price
