import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.slider import Click_slider


# Опции браузера

@allure.description("Test about link")
def test_slider():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    click_slider = Click_slider(driver)
    click_slider.sliders()