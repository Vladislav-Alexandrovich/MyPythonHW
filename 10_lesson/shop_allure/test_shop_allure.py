"""
Это автотест для проверки корректной работы сайта интернет-магазина,
можно подставлять разные значения указанных типов данных.
Сумма заказа должна быть равна указанной стоимости
"""
import allure
import pytest
from selenium import webdriver

from shop_pages_allure.auth_page import AuthPage
from shop_pages_allure.main_page import MainPage
from shop_pages_allure.cart_page import CartPage
from shop_pages_allure.order_page import OrderPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.epic("Магазин Saucedemo")
@allure.suite("Тесты на корректность оформления заказа")
@allure.severity("blocker")
@allure.story("Заказ товаров")
@allure.id("Saucedemo-1")
@allure.title("Проверка совпадения суммы заказа с указанной стоимостью")
@allure.description("Значения указанной стоимости"
                    "и суммы заказа должны быть одинаковы")
@allure.feature("TEST")
def test_shop(driver):
    Auth_Page = AuthPage(driver)
    login: str = "standard_user"
    password: str = "secret_sauce"
    Auth_Page.fill_login_fields(login, password)

    Main_Page = MainPage(driver)
    Main_Page.put_in_cart()

    Cart_Page = CartPage(driver)
    Cart_Page.checkout()

    Order_Page = OrderPage(driver)
    Order_Page.fill_order_details("Владислав", "Шахов", 188300)

    total_price = Order_Page.get_total_price()
    expected_price: float = 58.29

    with allure.step("Проверить что значения равны"):
        assert total_price == expected_price

    driver.quit()
