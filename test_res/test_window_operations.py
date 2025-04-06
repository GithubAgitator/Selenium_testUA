import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.window_operations import Window_operations


# Опции браузера

@allure.description("Test about link")
def test_window_operations():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_window_operations = Window_operations(driver)
    click_window_operations.window_operations()