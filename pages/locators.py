from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "[name ='login']")
    USERNAME = (By.CSS_SELECTOR, "[id = 'username']")
    PASSWORD = (By.CSS_SELECTOR, "[id = 'password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[id='submit_btn']")
    FIRSTLOGIN_FORM = (By.CSS_SELECTOR, "[class='firstlogin-title consent-firstlogin-title']")
    ACCEPT_CHECKBOX = (By.CSS_SELECTOR, "[type='checkbox']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[name='continue_button']")
    USER_INFO_FORM = (By.XPATH, "//span[text()='Setup your user information']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "[name='next_button']")
    TIME_DATE_FORM = (By.XPATH, "//span[text()= 'Set your time zone, date, and name formats']")
    START_BUTTON = (By.CSS_SELECTOR, "[name='start_sugar_button']")
    STARTSUGAR_FORM = (By.XPATH, "//span[text()= 'Start using Sugar!']")


class HomePageLocators:
    SUGAR_LOGO = (By.CSS_SELECTOR, "[title='SugarCRM']")

