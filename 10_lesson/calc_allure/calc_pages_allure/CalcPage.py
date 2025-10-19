"""
Этот класс содержит функции для тестирования медленного калькулятора,
переменные передаются из файла теста
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    @allure.feature("CREATE")
    @allure.step("Создание драйвера {browser}")
    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser

    @allure.feature("OPEN")
    @allure.step("Открытие сайта калькулятора")
    def open_calculator(self) -> None:
        self.browser.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        self.browser.fullscreen_window()

    @allure.feature("INPUT")
    @allure.step("Ввод значения задержки {term}")
    def set_delay(self, term: int) -> None:
        self.browser.find_element(By.ID, "delay").clear()
        self.browser.find_element(By.ID, "delay").send_keys(term)

    @allure.feature("CLICK")
    @allure.step("Клики по клавишам калькулятора {term1}, {term2}, {term3}")
    def buttons_clicks(self, term1: int, term2: str, term3: int) -> None:
        with allure.step("Клики по клавишам"):
            button_locator = "//span[text()='{}']"

            with allure.step("Первый клик - первое число {term1}"):
                first_number = self.browser.find_element(
                    By.XPATH, button_locator.format(term1))
                first_number.click()

            with allure.step("Второй клик - математическая операция {term2}"):
                operation_button = self.browser.find_element(
                    By.XPATH, button_locator.format(term2))
                operation_button.click()

            with allure.step("Третий клик - второе число {term3}"):
                second_number = self.browser.find_element(
                    By.XPATH, button_locator.format(term3))
                second_number.click()

            with allure.step("Четвертый клик на '='"):
                self.browser.find_element(By.XPATH,
                                          "//span[text()='=']").click()

    @allure.feature("GET")
    @allure.step("Получение после ожидания {term}"
                 "значения результата {term2} ")
    def get_result(self, term: int, term2: int) -> int:
        with allure.step("Ожидание появления результата {term2}"):
            waiter = WebDriverWait(self.browser, int(term) + 3)
            waiter.until(EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '[class="screen"]'), term2))

        with allure.step("Нахождение результата на странице"):
            result = self.browser.find_element(
                By.CSS_SELECTOR, '[class="screen"]').text

        with allure.step("Передача значения результата в тест {result}"):
            return result


# class CalcMainPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 5)
#
#     def open(self):
#         self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
#                         "slow-calculator.html")
#
#     def set_delay(self, delay):
#         delay_input = self.driver.find_element(By.ID, "delay")
#         delay_input.clear()
#         delay_input.send_keys(delay)
#
#     def click_button(self, button):
#         self.driver.find_element(
#             By.XPATH, f"//span[text()='{button}']").click()
#
#     def click_buttons(self, buttons):
#         for button in buttons:
#             self.click_button(button)
#
#     def wait_for_result(self, expected_result, delay):
#         # Добавляем +1 секунду к задержке для надежности
#         WebDriverWait(self.driver, delay + 1).until(
#             EC.text_to_be_present_in_element((
#                 By.CLASS_NAME, "screen"), expected_result)
#         )
#
#     def get_result(self):
#         return self.driver.find_element(By.CLASS_NAME, "screen").text