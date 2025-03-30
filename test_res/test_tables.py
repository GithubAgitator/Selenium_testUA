import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.tables import Click_tables


# Опции браузера

@allure.description("Test about link")
def test_tables():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_tables = Click_tables(driver)
    click_tables.tables()