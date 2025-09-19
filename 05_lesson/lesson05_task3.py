from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

input_box_locator = "input"

input_box = driver.find_element(By.CSS_SELECTOR, input_box_locator)

input_box.send_keys("Sky")

sleep(2)

input_box.clear()

sleep(2)

input_box.send_keys("Pro")

sleep(2)

driver.quit()
