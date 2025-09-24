import pytest
from selenium import webdriver
from calc_pages.CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc_result(driver):

    delay = "5"
    button1 = "7"
    button2 = "8"
    operation = "+"
    to_be = "15"

    calculator = CalcPage(driver)
    calculator.open_calculator()
    calculator.set_delay(delay)
    calculator.buttons_clicks(button1, operation, button2)
    as_is = calculator.get_result(delay, to_be)

    assert int(as_is) == int(to_be)
