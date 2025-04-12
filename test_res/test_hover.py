import time

import allure
from selenium import webdriver
from pages.hover import Hover


# Опции браузера

@allure.description("Test about link")
def test_hover():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_hover = Hover(driver)
    click_hover.hovers()