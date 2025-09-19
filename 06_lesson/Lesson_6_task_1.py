from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# вариант из теории
# driver.implicitly_wait(16)

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

waiter = WebDriverWait(driver, 16)

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content"),
                                     "Data loaded with AJAX get request.")
)

content = driver.find_element(By.CSS_SELECTOR, "#content")

txt = content.find_element(By.CLASS_NAME, "bg-success").text

print(txt)

driver.quit()
