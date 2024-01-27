from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, "loginForm__PjCel")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.TAG_NAME, "button")