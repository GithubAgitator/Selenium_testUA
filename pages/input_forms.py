import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Forms_page(Base):
    url = 'https://practice-automation.com/form-fields/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    name = "//input[@id='name-input']"
    password = "//input[@type='password']"
    drink1= "//input[@id='drink1']"
    drink2 = "//input[@id='drink2']"
    drink4 = "//input[@id='drink4']"
    color4 = "//input[@id='color4']"
    automation_meni = "//select[@id='automation']"
    yes = "//option[@value='yes']"
    email = "//input[@id='email']"
    message = "//textarea[@id='message']"
    button = "//button[@id='submit-btn']"
    water = "//label[text()='Water']"
    milk = "//label[text()='Milk']"
    wine = "//label[text()='Wine']"
    green = "//label[text()='Green']"




    #Getters
    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.password)))

    def get_drink1(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", self.drink1)))

    def get_water(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", self.water)))


    def get_drink2(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.drink2)))

    def get_milk(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", self.milk)))

    def get_drink4(self):
        element = self.driver.find_element("xpath", self.drink4)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_wine(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", self.wine)))

    def get_color4(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("xpath", self.color4)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        return element

    def get_green(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", self.green)))

    def get_automation_meni(self):
        return self.driver.find_element("xpath", self.automation_meni)

    def get_yes(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.yes)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.email)))

    def get_message(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.message)))

    def get_button(self):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.button)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        return element





    # Actions
    def input_name(self, name):
        self.get_name().send_keys(name)
        print("Input name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_drink1(self):
        self.get_drink1().click()
        print("Click drink1")

    def click_drink2(self):
        self.get_drink2().click()
        print("Click drink2")

    def click_drink4(self):
        self.get_drink4().click()
        print("Click drink4")

    def click_color4(self):
        self.get_color4().click()
        print("Click color4")

    def click_get_automation_meni(self):
        self.get_automation_meni().click()
        print("Click get_automation_meni")

    def click_yes(self):
        self.get_yes().click()
        print("Click yes")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_message(self, message):
        self.get_message().send_keys(message)
        print("Input message")

    def click_button(self):
        self.get_button().click()
        print("Click button login")

    def click_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        print('Click alert')





    #Methods
    def forms_input(self):
        with allure.step("Input forms"):
            Logger.add_start_step(method="Input forms")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_name('Daria')
            self.input_password('secret_sauce')
            self.click_drink1()
            self.assert_word(self.get_water(), 'Water')
            self.click_drink2()
            self.assert_word(self.get_milk(), 'Milk')
            self.click_drink4()
            self.assert_word(self.get_wine(), 'Wine')
            time.sleep(2)
            self.click_color4()
            self.assert_word(self.get_green(), 'Green')
            time.sleep(2)
            self.click_get_automation_meni()
            self.click_yes()
            self.input_email("fil20@gmail.com")
            self.input_message("Hello")
            time.sleep(2)
            self.click_button()
            time.sleep(2)
            self.click_alert()
            Logger.add_end_step(url=self.driver.current_url, method="Input forms")