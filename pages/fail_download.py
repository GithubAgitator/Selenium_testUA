import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Fail_download(Base):
    url = 'https://practice-automation.com/file-download/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    fail_1 = "//*[@id='post-1042']/div/div[1]/div/div/div/div[3]/a"
    fail_2 = "//*[@id='post-1042']/div/div[3]/div/div/div/div[3]/a"
    password = "//input[@name='password' and @type='password']"
    btn = "//input[@type='submit']"
    btn_closed = "//button[@class='close btn btn-link p-0']"
    form = "//*[@id='wpdm-lock-frame']"
    a = "//*[@id='wpdm-lock-options']"



    # Getters
    def get_fail_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.fail_1)))

    def get_fail_2(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.fail_2)))

    def get_form(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.form)))


    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.password)))

    def get_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.btn)))

    def get_btn_closed(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.btn_closed)))


        # Actions
    def click_fail_1(self):
        self.get_fail_1().click()

    def click_fail_2(self):
        self.get_fail_2().click()

    def click_form(self):
        self.driver.switch_to.frame(self.get_form())


    def c_input_password(self):
        self.get_input_password().send_keys("automateNow")

    def click_btn(self):
        self.get_btn().click()

    def click_btn_closed(self):
        self.get_btn_closed().click()


    def fail_download(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_fail_1()
            self.click_fail_2()
            self.click_form()
            self.c_input_password()
            self.click_btn()
            self.click_btn_closed()
            self.get_screenshot()
            time.sleep(1)
            Logger.add_end_step(url=self.driver.current_url, method="fail_download")




