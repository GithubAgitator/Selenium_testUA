import time

import allure
from selenium import webdriver
from pages.iframes import Click_iframe


# Опции браузера

@allure.description("Test about link")
def test_iframe():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_iframe = Click_iframe(driver)
    click_iframe.iframe()