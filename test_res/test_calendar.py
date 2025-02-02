import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.calendar import Click_calendars


# Опции браузера

@allure.description("Test about link")
def test_slider():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_next_month = Click_calendars(driver)
    click_next_month.calendars()