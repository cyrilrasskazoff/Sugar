from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "[name ='login']")
    USERNAME = (By.CSS_SELECTOR, "[id = 'username']")
    PASS = (By.CSS_SELECTOR, "[id = 'password']")
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


class SidebarLocators:
    HAMBURGER_MENU = (By.ID, "expand-menu_sidebar-nav-item")
    ACCOUNTS_MENU_LINK = (By.ID, 'Accounts_sidebar-nav-item')


class ListViewLocators:
    BUILD_FILTER_BUTTON = (By.XPATH, "//span[text()= 'Build Filter']")
    CREATE_BUTTON = (By.NAME, "create_button")


class AccountsPageLocators:
    ACCOUNTS_TITLE = (By.XPATH, '//*[@id="content"]/div/div/div[1]/div[2]/div/h1/span[1]/span/span/span/div')
    NAME_INPUT = (By.CSS_SELECTOR, "[aria-label='Name']")
    SAVE_BUTTON = (By.NAME, "save_button")
    ACCOUNT_RECORDS = (By.CSS_SELECTOR, "[class = 'ellipsis_inline Accounts']")












