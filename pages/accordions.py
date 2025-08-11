import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Accordins(Base):
    url = 'https://practice-automation.com/accordions/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button = "//summary[text()='Click to see more']"
    res_text = "//p[text()='This is an accordion item.']"


    # Getters
    def get_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.button)))

    def get_res_text(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.res_text)))
        element = self.driver.find_element("xpath", self.res_text)
        return element.text

        # Actions
    def click_button(self):
        self.get_button().click()





    def accordins(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_button()
            assert self.get_res_text() == 'This is an accordion item.'
            time.sleep(5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="accordinst")
