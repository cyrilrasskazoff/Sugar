from .base_page import BasePage
from .locators import HomePageLocators
import selenium.common
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage(BasePage):
    def should_be_home_page(self):
        self.should_be_home_url()
        self.should_be_sugar_logo()
        self.should_be_hamburger_menu()

    def should_be_home_url(self):
        assert "Home" in self.driver.current_url, "This is not a Home page"

    def should_be_sugar_logo(self):
        assert self.is_element_present(*HomePageLocators.SUGAR_LOGO), "Not a Home page or Sugar Logo is missing"

    def should_be_hamburger_menu(self):
        assert self.is_element_present(*HomePageLocators.HAMBURGER_MENU), "Not a Home page or Hamburger Menu is missing"
        print("Home Page is displayed")

    def accounts_link_navigates_to_accounts_page(self):
        hamburger = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(HomePageLocators.HAMBURGER_MENU))
        hamburger.click()
        accounts_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(HomePageLocators.ACCOUNTS_MENU_LINK))
        accounts_link.click()




