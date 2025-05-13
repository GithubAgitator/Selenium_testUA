import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.gestures import Gestures


# Опции браузера

@allure.description("Test about link")
def test_gestures():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_move = Gestures(driver)
    click_move.gestures()