import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains

class Gestures(Base):
    url = 'https://practice-automation.com/gestures/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    move = "//div[@id='moveMeHeader']"
    move_drop = "//*[@id='post-1023']/div/p[2]"
    automate_now = "//div[@id='div1']"
    automate_now_drop = "//div[@id='div2']"
    drag = "//*[@id='post-1023']/div/p[4]"
    lake_man = "//*[@id='post-1023']/div/div[6]"
    lake_man_drop = "//*[@id='post-1023']/div/div[6]/div/div/div/div/div"




    # Getters
    def get_move(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.move)))

    def get_move_drop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.move_drop)))

    def get_automate_now(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.automate_now)))

    def get_automate_now_drop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.automate_now_drop)))

    def get_drag(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("xpath", self.drag)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        return element


    def get_lake_man(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.lake_man)))

    def get_lake_man_drop(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.lake_man_drop)))

        # Actions
    def click_move(self):
        ActionChains(self.driver).drag_and_drop(self.get_move(), self.get_move_drop()).perform()

    def click_automate_now(self):
        ActionChains(self.driver).drag_and_drop(self.get_automate_now(), self.get_automate_now_drop()).perform()

    def click_lake_man(self):
        element1 = self.get_lake_man()
        element2 = self.get_lake_man_drop()
        action = ActionChains(self.driver)
        action.drag_and_drop(element1, element2).perform()







    def gestures(self):
        with allure.step("time javaScripts"):
            Logger.add_start_step(method="time javaScripts")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_move()
            self.click_automate_now()
            self.get_drag()
            self.click_lake_man()
            time.sleep(5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="gestures")
