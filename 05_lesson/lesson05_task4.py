from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

input_username_locator = "username"
input_username = driver.find_element(By.ID, input_username_locator)
input_username.send_keys("tomsmith")

sleep(2)

input_password_locator = "password"
input_password = driver.find_element(By.ID, input_password_locator)
input_password.send_keys("SuperSecretPassword!")

sleep(2)

signbutton_locator = "button.radius"
signbutton = driver.find_element(By.CSS_SELECTOR, signbutton_locator)
signbutton.click()

sleep(2)

greentext_locator = "div.flash.success"
greentext = driver.find_element(By.CSS_SELECTOR, greentext_locator).text
print(greentext)

driver.quit()
