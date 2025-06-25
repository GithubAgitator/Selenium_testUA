import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.fail_download import Fail_download


# Опции браузера

@allure.description("Test about link")
def test_fdownload():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    downloads = Fail_download(driver)
    downloads.fail_download()
