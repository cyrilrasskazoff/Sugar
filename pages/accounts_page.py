from .base_page import BasePage
from .list_vew_page import ListViewPage
from .locators import AccountsPageLocators
from .locators import ListViewLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


class AccountsPage(ListViewPage): # наследует ListViewPage (который в свою очередь наследует BasePage)
    account_name = "test" + str(random.randint(1, 999999))

    def should_be_accounts_page(self):
        self.should_be_accounts_url()
        self.should_be_accounts_title()
        self.should_be_list_vew()

    def should_be_accounts_url(self):
        assert "Accounts" in self.driver.current_url, "This is not an Accounts page"

    def should_be_accounts_title(self):
        acc_title = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(AccountsPageLocators.ACCOUNTS_TITLE))
        assert "Accounts" in acc_title.text, "Not an Accounts page or no Accounts title"
        print("Accounts List View page is displayed")

    def should_create_account_with_required_fields(self):
        create_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ListViewLocators.CREATE_BUTTON))
        create_btn.click()
        name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AccountsPageLocators.NAME_INPUT))
        name_input.send_keys(AccountsPage.account_name)
        save_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AccountsPageLocators.SAVE_BUTTON))
        save_btn.click()
        time.sleep(5)





