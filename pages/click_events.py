import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Click_evants(Base):
    url = 'https://practice-automation.com/click-events/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    btn_cat = "//*[@id='post-3145']/div/div[3]/div/div/div/div[1]/button"
    meow = "//h2[text()='Meow!']"
    btn_dog = "//*[@id='post-3145']/div/div[3]/div/div/div/div[2]/button"
    woof = "//h2[text()='Woof!']"
    btn_pig = "//*[@id='post-3145']/div/div[5]/div[1]/button"
    oink = "//h2[text()='Oink!']"
    btn_cow = "//*[@id='post-3145']/div/div[5]/div[2]/button"
    moo = "//h2[text()='Moo!']"


    # Getters
    def get_btn_cat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.btn_cat)))

    def get_meow(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.meow)))
        element = self.driver.find_element("xpath", self.meow)
        return element.text

    def get_btn_dog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.btn_dog)))

    def get_woof(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.woof)))
        element = self.driver.find_element("xpath", self.woof)
        return element.text

    def get_btn_pig(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.btn_pig)))

    def get_oink(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.oink)))
        element = self.driver.find_element("xpath", self.oink)
        return element.text

    def get_btn_cow(self):
       return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.btn_cow)))

    def get_moo(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.moo)))
        element = self.driver.find_element("xpath", self.moo)
        return element.text



        # Actions
    def click_btn_cat(self):
        self.get_btn_cat().click()


    def click_btn_dog(self):
        self.get_btn_dog().click()

    def click_btn_pig(self):
        self.get_btn_pig().click()

    def click_btn_cow(self):
        self.get_btn_cow().click()


    def click_events(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_btn_cat()
            assert self.get_meow() == 'Meow!'
            print('Meow!')
            self.click_btn_dog()
            assert self.get_woof() == 'Woof!'
            print('Woof!')
            self.click_btn_pig()
            assert self.get_oink() == 'Oink!'
            print('Oink!')
            self.click_btn_cow()
            assert self.get_moo() == 'Moo!'
            print('Moo!')
            self.get_screenshot()
            time.sleep(1)
            Logger.add_end_step(url=self.driver.current_url, method="click_events")




