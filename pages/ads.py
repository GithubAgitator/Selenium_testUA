import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Ads(Base):
    url = 'https://practice-automation.com/ads/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button = "//button[@class='pum-close popmake-close']"


    # Getters
    def get_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.button)))

        # Actions
    def click_button(self):
        self.get_button().click()





    def ads(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_button()
            time.sleep(5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="hover")
