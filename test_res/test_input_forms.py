import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.input_forms import Forms_page


# Опции браузера

@allure.description("Test about link")
def test_forms():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    input_forms = Forms_page(driver)
    input_forms.forms_input()