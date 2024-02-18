from .base_page import BasePage
from .locators import AccountsPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountsPage(BasePage):
    def should_be_accounts_page(self):
        self.should_be_accounts_url()
        self.should_be_accounts_title()

    def should_be_accounts_url(self):
        assert "Accounts" in self.driver.current_url, "This is not an Accounts page"

    def should_be_accounts_title(self):
        acc_title = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(AccountsPageLocators.ACCOUNTS_TITLE))
        assert "Accounts" in acc_title.text, "Not an Accounts page or no Accounts title"
        print("Accounts page is displayed")


