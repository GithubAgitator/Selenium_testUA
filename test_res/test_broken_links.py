import time

import allure
from selenium import webdriver
from pages.broken_links import BrokenLinks


# Опции браузера

@allure.description("Test about link")
def test_broken_links():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_button = BrokenLinks(driver)
    click_button.broken_links()