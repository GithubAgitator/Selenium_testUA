import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Click_calendars(Base):
    url = 'https://practice-automation.com/calendars/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    selectorenteradate = "//input[@id='g1065-2-selectorenteradate']"
    selectorenteradate_total = "//input[@value='2025-09-01']"
    nexts = "//*[@id='ui-datepicker-div']/div/a[2]"
    month = "//*[@id='ui-datepicker-div']/div/div/span[1]"
    day = "//a[text()='1']"
    btn = "//button[@type='submit']"

    # Getters
    def get_selectorenteradate(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.selectorenteradate)))

    def get_month(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.month)))
        element = self.driver.find_element("xpath", self.month)
        return element.text

    def get_next(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.nexts)))

    def get_day(self):
       return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.day)))

    def get_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.btn)))

        # Actions
    def click_selectorenteradate(self):
        self.get_selectorenteradate().click()

    def click_next(self):
        while True:
            current_month = self.get_month()
            if current_month == 'September':
                break
            self.get_next().click()

    def click_day(self):
        self.get_day().click()

    def click_btn(self):
        self.get_btn().click()



    def calendars(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_selectorenteradate()
            self.click_next()
            self.click_day()
            self.get_screenshot()
            time.sleep(1)
            self.click_btn()




