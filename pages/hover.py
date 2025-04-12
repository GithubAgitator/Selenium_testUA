import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Hover(Base):
    url = 'https://practice-automation.com/hover/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    hover = "//h3[@id='mouse_over']"

    # Getters
    def get_hover(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.hover)))

        # Actions
    def click_hover(self):
        self.get_hover().click()


    def hovers(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_hover()
            self.assert_word(self.get_hover(), "You did it!")
            time.sleep(5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="hover")
