import time

import allure
from selenium import webdriver
from pages.accordions import Accordins


# Опции браузера

@allure.description("Test about link")
def test_accordins():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_button = Accordins(driver)
    click_button.accordins()