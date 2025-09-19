import pytest
from selenium import webdriver

from shop_pages.auth_page import AuthPage
from shop_pages.main_page import MainPage
from shop_pages.cart_page import CartPage
from shop_pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_shop(driver):
    Auth_Page = AuthPage(driver)
    login = "standard_user"
    password = "secret_sauce"
    Auth_Page.fill_login_fields(login, password)

    Main_Page = MainPage(driver)
    Main_Page.put_in_cart()

    Cart_Page = CartPage(driver)
    Cart_Page.checkout()

    Order_Page = OrderPage(driver)
    Order_Page.fill_order_details("Владислав", "Шахов", "188300")

    total_price = Order_Page.get_total_price()
    expected_price = "Total: $58.29"

    assert total_price == expected_price

    driver.quit()
