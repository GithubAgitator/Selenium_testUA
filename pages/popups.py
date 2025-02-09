import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Click_popups(Base):
    url = 'https://practice-automation.com/popups/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    alert = "//button[@id='alert']"
    confirm = "//button[@id='confirm']"
    confirm_res_no = "//*[@id='confirmResult']"
    prompt = "//button[@id='prompt']"
    prompt_res = "//*[@id='promptResult']"
    tooltip_1 = "//div[@class='tooltip_1']"
    tooltip_1_res = "//span[@id='myTooltip']"


    # Getters
    def get_alert(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.alert)))

    def get_confirm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.confirm)))

    def get_confirm_res_no(self):
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(("xpath", self.confirm_res_no), 'Cancel it is!'))
        element = self.driver.find_element("xpath", self.confirm_res_no)
        return element.text
    def get_prompt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.prompt)))

    def get_prompt_res(self):
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(("xpath", self.prompt_res), 'Nice to meet you, Hello!'))
        element = self.driver.find_element("xpath", self.prompt_res)
        return element.text

    def get_tooltip_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.tooltip_1)))

    def get_tooltip_1_res(self):
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(("xpath", self.tooltip_1_res), 'Cool text'))
        element = self.driver.find_element("xpath", self.tooltip_1_res)
        return element.text

        # Actions

    def click_alert(self):
        self.get_alert().click()


    def click_alert_1(self):
        alert = self.driver.switch_to.alert
        assert alert.text == 'Hi there, pal!'
        time.sleep(2)
        alert.accept()

    def click_confirm(self):
        self.get_confirm().click()



    def click_alert_2(self):
        alert = self.driver.switch_to.alert
        assert alert.text == 'OK or Cancel, which will it be?'
        alert.dismiss()

    def click_prompt(self):
        self.get_prompt().click()

    def click_alert_3(self):
        alert = self.driver.switch_to.alert
        alert.send_keys("Hello")
        alert.accept()

    def click_tooltip_1(self):
        self.get_tooltip_1().click()


    def popups_clicks(self):
        with allure.step("popups"):
            Logger.add_start_step(method="popups")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_alert()
            self.click_alert_1()
            print('Hi there, pal!')
            self.click_confirm()
            time.sleep(2)
            self.click_alert_2()
            time.sleep(2)
            assert self.get_confirm_res_no() == 'Cancel it is!'
            self.click_prompt()
            self.click_alert_3()
            assert self.get_prompt_res() == 'Nice to meet you, Hello!'
            self.click_tooltip_1()
            assert self.get_tooltip_1_res() == 'Cool text'
            time.sleep(2)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="popups")
