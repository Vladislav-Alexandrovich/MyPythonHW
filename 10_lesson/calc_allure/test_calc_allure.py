"""
Это автотест для проверки функции сложения медленного калькулятора,
можно подставлять разные значения указанных типов данных
"""
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

from calc_pages_allure.CalcPage import CalcPage


@pytest.fixture
def driver() -> None:
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.epic("Медленный калькулятор")
@allure.suite("Тесты вычислений на медленном калькуляторе")
@allure.severity("trivial")
@allure.story("Сложение")
@allure.id("Калькулятор-1")
@allure.title("Проверка правильности результата сложения двух"
              "значений после прошествия интервала")
@allure.description("Результат математических действий"
                    "должен совпадать с заданным")
@allure.feature("TEST")
@allure.step("Проверить что значения вычислений совпадают с заявленным")
def test_calc_result(driver: WebDriver) -> None:

    """
    Передаваемые данные для математических действий"
    "{delay}, {button1}, {button3}, {operation}, {to_be}")
    """

    delay: int = "5"
    button1: int = "7"
    button2: int = "8"
    operation: str = "+"
    to_be: int = "15"

    calculator = CalcPage(driver)

    # with allure.step("Открыть сайт калькулятора"):
    calculator.open_calculator()

    # with allure.step("Выставить значение задержки вывода результата"):
    calculator.set_delay(delay)

    # with allure.step("Кликнуть на заданные клавиши"):
    calculator.buttons_clicks(button1, operation, button2)
    as_is = calculator.get_result(delay, to_be)

    with allure.step("Проверить что значения равны"):
        assert int(as_is) == int(to_be)
