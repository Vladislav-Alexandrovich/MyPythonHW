from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

waiter = WebDriverWait(driver, 30)

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text.lead"), "Done")
)

# длинный вариант
# picture3 = driver.find_element(By.ID, "award")

# picture3_src = picture3.get_attribute("src")

# print(f"image 3 src: {picture3_src}")

image3_src = driver.find_element(By.ID, "award").get_attribute("src")

print("image 3 src:", image3_src)

driver.quit()
