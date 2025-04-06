import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Window_operations(Base):
    url = 'https://practice-automation.com/window-operations/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators
    new_tab = "//*[@id='post-1147']/div/p[3]/button"
    replace_window = "//*[@id='post-1147']/div/p[5]/button"
    new_window = "//*[@id='post-1147']/div/p[7]/button"

    # Getters
    def get_new_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.new_tab)))

    def get_replace_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.replace_window)))

    def get_new_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.new_window)))

    def window(self):
        return self.driver.window_handles

        # Actions
    def click_new_tab(self):
        self.get_new_tab().click()


    def click_replace_window(self):
        self.get_replace_window().click()
        self.get_screenshot()
        self.driver.back()

    def click_new_window(self):
        self.get_new_window().click()
        self.driver.switch_to.window(self.window()[-1])
        self.get_screenshot()
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(self.window()[0])


    def window_operations(self):
        with (allure.step("time javaScripts")):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.window()
            self.driver.maximize_window()
            self.get_current_url()
            self.click_new_tab()
            self.driver.switch_to.window(self.window()[0])
            self.assert_url('https://practice-automation.com/window-operations/')
            self.click_replace_window()
            self.assert_url('https://practice-automation.com/window-operations/')
            self.click_new_window()
            self.assert_url('https://practice-automation.com/window-operations/')
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="window_operations")
