from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_optional_element_present(self, method, element, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((method, element)))
        except (NoSuchElementException, TimeoutException):
            return False
        pass

    def is_element_present(self, method, element, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((method, element)))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def is_not_element_present(self, method, element, timeout=10):  # метод, который проверяет, что элемент не появляется на
        # странице в течение заданного времени
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((method, element)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, method, element, timeout=10):  # метод, который проверяет, что элемент исчезнет со страницы по
        # истечении заданного времени
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((method, element)))  # # 3 аргумент означает частоту опроса, Т.е.
            # WebDriver ждёт 10 секунды и делает запросы каждую секунду
        except TimeoutException:
            return False
        return True


