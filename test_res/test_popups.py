import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.popups import Click_popups


# Опции браузера

@allure.description("Test about link")
def test_popups():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_popups = Click_popups(driver)
    click_popups.popups_clicks()