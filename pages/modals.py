import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Click_modals(Base):
    url = 'https://practice-automation.com/modals/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    simpleModal = "//button[@id='simpleModal']"
    close = " //*[@id='popmake-1318']/button"
    formModal = "//button[@id='formModal']"
    name = "//input[@id='g1051-name']"
    email = "//input[@id='g1051-email']"
    text = "//textarea[@id='contact-form-comment-g1051-message']"
    btn = "//button[@class='pushbutton-wide']"
    modals = "//*[@id='top-wrap']/section/div/h1"

    # Getters
    def get_simpleModal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.simpleModal)))

    def get_close(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.close)))

    def get_formModal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.formModal)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.email)))

    def get_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.text)))

    def get_btn(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("xpath", self.btn)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        return element

    def get_modals(self):
        element = self.driver.find_element("xpath", self.modals)
        return element.text

        # Actions
    def click_simpleModal(self):
        self.get_simpleModal().click()

    def click_close(self):
        self.get_close().click()

    def click_formModal(self):
        self.get_formModal().click()

    def input_name(self):
        self.get_name().send_keys("Marina")

    def input_email(self):
        self.get_email().send_keys("marina@gmail.com")

    def input_text(self):
        self.get_text().send_keys("Hello!")

    def click_btn(self):
        self.get_btn().click()


    def modals(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_simpleModal()
            self.click_close()
            self.click_formModal()
            self.input_name()
            self.input_email()
            self.input_text()
            self.click_btn()
            self.get_screenshot()
            assert self.assert_word(self.get_modals(), 'Modals')
