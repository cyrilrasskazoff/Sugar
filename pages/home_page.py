from .base_page import BasePage
from .locators import HomePageLocators


class HomePage(BasePage):
    def should_be_home_page(self):
        self.should_be_sugar_logo()

    def should_be_sugar_logo(self):
        assert self.is_element_present(*HomePageLocators.SUGAR_LOGO), "Not Home page or Sugar Logo is missing"
        print("Home Page is displayed")

