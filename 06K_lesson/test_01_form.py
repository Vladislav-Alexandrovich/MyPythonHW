import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Safari()
    return driver


def test_fill_and_submit_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.fullscreen_window()

    driver.find_element(
        By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "[name='phone']").send_keys("+798589998787")
    driver.find_element(
        By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button").click()

    driver.fullscreen_window()

    waiter = WebDriverWait(driver, 4)

    waiter.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#zip-code"), "N/A"))

    red_color = "rgb(248, 215, 218)"
    green_color = "rgb(209, 231, 221)"

    first_name_color = driver.find_element(
        By.ID, "first-name").value_of_css_property("background-color")

    # print(first_name_color)

    assert first_name_color == green_color

    last_name_color = driver.find_element(
        By.ID, "last-name").value_of_css_property("background-color")

    assert last_name_color == green_color

    address_color = driver.find_element(
        By.ID, "address").value_of_css_property("background-color")

    assert address_color == green_color

    address_color = driver.find_element(
        By.ID, "address").value_of_css_property("background-color")

    assert address_color == green_color

    country_color = driver.find_element(
        By.ID, "country").value_of_css_property("background-color")

    assert country_color == green_color

    e_mail_color = driver.find_element(
        By.ID, "e-mail").value_of_css_property("background-color")

    assert e_mail_color == green_color

    phone_number_color = driver.find_element(
        By.ID, "phone").value_of_css_property("background-color")

    assert phone_number_color == green_color

    job_position_color = driver.find_element(
        By.ID, "job-position").value_of_css_property("background-color")

    assert job_position_color == green_color

    company_color = driver.find_element(
        By.ID, "company").value_of_css_property("background-color")

    assert company_color == green_color

    zip_code_color = driver.find_element(
        By.ID, "zip-code").value_of_css_property("background-color")

    # print(zip_code_color)

    assert zip_code_color == red_color

    driver.quit()


# пример другого решения

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     return driver

# def test_fill_and_submit_form(driver):
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

#     driver.find_element(
#         By.CSS_SELECTOR, "input[name=first-name]").send_keys("Иван")
#     driver.find_element(
#         By.CSS_SELECTOR, "input[name=last-name]").send_keys("Петров")
#     driver.find_element(
#         By.CSS_SELECTOR, "input[name=address").send_keys("Ленина, 55-3")
#     driver.find_element(
#         By.CSS_SELECTOR, "input[name=e-mail]").send_keys("test@skypro.com")
#     driver.find_element(
#         By.CSS_SELECTOR, "input[name=phone]").send_keys("+7985899998787")
#     driver.find_element(
#         By.CSS_SELECTOR, "input[name=zip-code]").send_keys("")
#     driver.find_element(
#         By.CSS_SELECTOR, "input[name=city]").send_keys("Москва")
#     driver.find_element(
#         By.CSS_SELECTOR, "input[name=country]").send_keys("Россия")
#     driver.find_element(
#         By.CSS_SELECTOR, "input[name=job-position]").send_keys("QA")
#     driver.find_element(
#         By.CSS_SELECTOR, "input[name=company]").send_keys("SkyPro")

#     submit_button = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located(
#             (By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3"))
#     )
#     driver.execute_script(
#         "arguments[0].scrollIntoView(true);", submit_button)
#     # Scroll to the button
#     driver.execute_script(
#         "arguments[0].click();", submit_button)

#     WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located(
#             (By.CSS_SELECTOR, "main[class=flex-shrink-2]"))
#     )

#     zip_code_field = driver.find_element(By.CSS_SELECTOR, "div#zip-code")
#     assert "alert-danger" in zip_code_field.get_attribute("class")

#     green_highlighted_fields = driver.find_elements(
#         By.CSS_SELECTOR, "div.alert.py-2.alert-success")
#     assert len(green_highlighted_fields) == 9
#     # Должно быть 9 успешно подсвеченных полей
