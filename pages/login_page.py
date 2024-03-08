from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .variables import PASSWORD, USER


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missing"

    def login_admin_and_navigate_to_home_page(self):
        password = PASSWORD
        user = USER
        user_name_field = self.driver.find_element(*LoginPageLocators.USERNAME)
        user_name_field.send_keys(user)
        password_field = self.driver.find_element(*LoginPageLocators.PASS)
        password_field.send_keys(password)
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(LoginPageLocators.FIRSTLOGIN_FORM))
        except (NoSuchElementException, TimeoutException):
            print("not first login or first_login form not found")
        else:
            accept_check = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(LoginPageLocators.ACCEPT_CHECKBOX))
            accept_check.click()
            continue_btn = self.driver.find_element(*LoginPageLocators.CONTINUE_BTN)
            continue_btn.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(LoginPageLocators.USER_INFO_FORM))
        except (NoSuchElementException, TimeoutException):
            print("Not first login or user_info form not found")
        else:
            next_btn = self.driver.find_element(*LoginPageLocators.NEXT_BUTTON)
            next_btn.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(LoginPageLocators.TIME_DATE_FORM))
        except (NoSuchElementException, TimeoutException):
            print("Not first login or time_date_form not found")
        else:
            next_btn = self.driver.find_element(*LoginPageLocators.NEXT_BUTTON)
            next_btn.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(LoginPageLocators.STARTSUGAR_FORM))
        except (NoSuchElementException, TimeoutException):
            print("Not first login or start_sugar form not found")
        else:
            start_btn = self.driver.find_element(*LoginPageLocators.START_BUTTON)
            start_btn.click()







