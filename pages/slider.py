import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Click_slider(Base):
    url = 'https://practice-automation.com/slider/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    slideMe = "//input[@id='slideMe']"

    # Getters
    def get_slideMe(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.slideMe)))

        # Actions
    def click_slideMe(self):
        actions = ActionChains(self.driver)
        actions.click_and_hold(self.get_slideMe()).move_by_offset(50, 0).release().perform()

    def sliders(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_slideMe()
            time.sleep(5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="slider")
