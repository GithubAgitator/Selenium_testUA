import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Click_iframe(Base):
    url = 'https://practice-automation.com/iframes/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    ifraMe1 = "//iframe[@id='iframe-1']"
    menu = "//span[text()='Playwright']"
    ifraMe2 = "//iframe[@id='iframe-2']"
    menu2 = "//p[text()='What you do with that power is entirely up to you.']"

    # Getters
    def get_ifraMe1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.ifraMe1)))


    def get_ifraMe2(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.ifraMe2)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element



    def get_menu(self):
        b = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.menu)))
        return b.text

    def get_menu2(self):
        b2 = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.menu2)))
        return b2.text


        # Actions
    def click_ifraMe1(self):
        self.driver.switch_to.frame(self.get_ifraMe1())


    def click_ifraMe2(self):
        self.driver.switch_to.frame(self.get_ifraMe2())


    def iframe(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_ifraMe1()
            assert self.get_menu() == 'Playwright'
            self.driver.switch_to.default_content()
            self.click_ifraMe2()
            assert self.get_menu2() == 'What you do with that power is entirely up to you.'
            time.sleep(5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="iframes")
