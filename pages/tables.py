import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Click_tables(Base):
    url = 'https://practice-automation.com/tables/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    orange = "//*[@id='post-1076']/div/figure/table/tbody/tr[2]/td[1]"
    orange_price = "//*[@id='post-1076']/div/figure/table/tbody/tr[2]/td[2]"
    country = "//*[@id='tablepress-1']/thead/tr/th[2]"
    btn_two = "//*[@id='tablepress-1_wrapper']/div[3]/div[2]/div/nav/button[3]"
    btn_three = "//*[@id='tablepress-1_wrapper']/div[3]/div[2]/div/nav/button[4]"
    russian = "//td[text()='Russia']"

    # Getters
    def get_orange(self):
        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element(("xpath", self.orange), 'Oranges'))
        element = self.driver.find_element("xpath", self.orange)
        return element.text


    def get_orange_price(self):
        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element(("xpath", self.orange_price), '$3.99'))
        element = self.driver.find_element("xpath", self.orange_price)
        return element.text

    def get_country(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.country)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_btn_two(self):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.btn_two)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_btn_three(self):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.btn_three)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_russian(self):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.russian)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element(("xpath", self.russian), 'Russia'))
        elements = self.driver.find_element("xpath", self.russian)
        print(elements)
        return elements.text

        # Actions
    def click_btn_two(self):
        self.get_btn_two().click()

    def click_btn_three(self):
        self.get_btn_three().click()


    def el(self):
        if 'Russia' not in self.get_russian():
            self.click_btn_two()
        if 'Russia' not in self.get_russian():
            self.click_btn_three()


    def tables(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            assert self.get_orange() == 'Oranges'
            assert self.get_orange_price() == '$3.99'
            self.get_country()
            time.sleep(5)
            self.el()
            assert self.get_russian() == 'Russia'
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="tables")
