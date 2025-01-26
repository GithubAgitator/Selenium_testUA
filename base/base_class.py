import datetime
import os


class Base():
    def __init__(self, driver):
        self.driver = driver
    url = 'https://dominopizza.ru/'

    """Method GET current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method screenshot"""
    def get_screenshot(self):
        """Создание скриншота"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        os.makedirs("screen", exist_ok=True)
        self.driver.save_screenshot(f"C:\\Users\\d.milyakova\\Desktop\\main_projects\\screen/{name_screenshot}")
        print("Скриншот выполнен")

    """Method assert url"""
    def assert_url(self, res):
        get_url = self.driver.current_url
        assert get_url == res
        print("Get value url")