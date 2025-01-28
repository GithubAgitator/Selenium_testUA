import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Click_javaScripts(Base):
    url = 'https://practice-automation.com/javascript-delays/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button = "//button[@id='start']"
    text = "//input[@id='delay']"

    # Getters
    def get_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.button)))

    def get_text(self):
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element_value(("xpath", self.text), 'Liftoff!'))
        element = self.driver.find_element("xpath", self.text)
        return element.get_attribute('value')
        # Actions
    def click_button(self):
        self.get_button().click()
        print("Click button")

    def c_Js(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_button()
            # print(self.get_text())
            assert self.get_text() == 'Liftoff!'
            print('Liftoff!')
            self.get_screenshot()
