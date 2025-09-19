import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    return driver


def test_right_price_in_the_cart(driver):
    driver.get("https://www.saucedemo.com/")

# логинизация

    driver.find_element(
        By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(
        By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(
        By.CSS_SELECTOR, "#login-button").click()

# выбор покупок

    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(
        By.CSS_SELECTOR, "a.shopping_cart_link").click()

# страница корзины

    driver.implicitly_wait(4)
    driver.find_element(By.ID, "checkout").click()
    driver.implicitly_wait(4)

# страница оформления заказа

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Владислав")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Шахов")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("188300")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

# страница подтверждения заказа

    total_price = driver.find_element(
        By.CSS_SELECTOR, "[data-test='total-label']").text

# "div.summary_total_label"
# "[data-test='total-label']"

    expected_price = "Total: $58.29"

    assert total_price == expected_price

    driver.quit()
