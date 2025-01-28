import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.time_javaScripts import Click_javaScripts


# Опции браузера

@allure.description("Test about link")
def test_time_Js():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_js = Click_javaScripts(driver)
    click_js.c_Js()