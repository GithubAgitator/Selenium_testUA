import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.click_events import Click_evants


# Опции браузера

@allure.description("Test about link")
def test_click_events():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_events = Click_evants(driver)
    click_events.click_events()
