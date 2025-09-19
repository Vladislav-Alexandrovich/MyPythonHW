import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


def test_fill_slow_calc(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator"
        )

    driver.find_element(By.ID, "delay").clear()

    driver.find_element(By.ID, "delay").send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()

    driver.find_element(By.XPATH, "//span[text()='+']").click()

    driver.find_element(By.XPATH, "//span[text()='8']").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='=']")))
    button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='=']")))
    driver.execute_script("arguments[0].click();", button)

    waiter = WebDriverWait(driver, 47)

    waiter.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    result = driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text

    expected_result = "15"

    assert result == expected_result

    driver.quit()
