from .base_page import BasePage
from .locators import ListViewLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ListViewPage(BasePage):
    def should_be_list_vew(self):
        self.should_be_build_filter_button()
        self.should_be_create_button()

    def should_be_build_filter_button(self):
        assert self.is_element_present(*ListViewLocators.BUILD_FILTER_BUTTON), "Not a ListView page or Build Filter" \
                                                                               "button is missing"

    def should_be_create_button(self):
        assert self.is_element_present(*ListViewLocators.CREATE_BUTTON), "Not a ListView page or Create " \
                                                                         "button is missing"