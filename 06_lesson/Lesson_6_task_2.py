from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


driver.get("http://uitestingplayground.com/textinput")

new_button = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
new_button.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

driver.implicitly_wait(4)

updated_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(updated_button)

driver.quit()
