from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, browser):
        self.browser = browser

    def open_calculator(self):
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, term):
        self.browser.find_element(By.ID, "delay").clear()
        self.browser.find_element(By.ID, "delay").send_keys(term)

    def buttons_clicks(self, term1, term2, term3):
        button_locator = "//span[text()='{}']"

        first_number = self.browser.find_element(
            By.XPATH, button_locator.format(term1))
        first_number.click()

        operation_button = self.browser.find_element(
            By.XPATH, button_locator.format(term2))
        operation_button.click()

        second_number = self.browser.find_element(
            By.XPATH, button_locator.format(term3))
        second_number.click()

        self.browser.find_element(By.XPATH, "//span[text()='=']").click()

        # self.browser.find_element(By.XPATH, "//span[text()='7']").click()
        # self.browser.find_element(By.XPATH, "//span[text()='+']").click()
        # self.browser.find_element(By.XPATH, "//span[text()='8']").click()
        # self.browser.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self, term, term2):
        waiter = WebDriverWait(self.browser, term + 3)
        waiter.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[class="screen"]'), term2))

        result = self.browser.find_element(
            By.CSS_SELECTOR, '[class="screen"]').text

        return result



# driver = webdriver.Firefox()
# # def open_calc(self):
    #     self.driver.get(
    #         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator")
    #     self.driver.fullscreen_window()
 # self.browser.quit()