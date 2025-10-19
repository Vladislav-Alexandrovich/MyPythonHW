from selenium.webdriver.common.by import By


class AuthPage:

    def __init__(self, browser):
        self.browser = browser

    def fill_login_fields(self, term1, term2):
        self.browser.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(term1)
        self.browser.find_element(
            By.CSS_SELECTOR, "#password").send_keys(term2)
        self.browser.find_element(
            By.CSS_SELECTOR, "#login-button").click()