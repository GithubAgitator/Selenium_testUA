import time

import allure
from selenium import webdriver
from pages.modals import Click_modals


# Опции браузера

@allure.description("Test about link")
def test_modals():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_modals = Click_modals(driver)
    click_modals.modals()