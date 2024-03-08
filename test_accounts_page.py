from .pages.login_page import LoginPage
from .pages.home_page import HomePage
from .pages.accounts_page import AccountsPage
from .pages.variables import URL


def test_admin_user_is_navigated_to_accounts_page_after_click_on_accounts(driver_login):
    url = URL
    page = HomePage(driver_login, url)
    page.accounts_link_navigates_to_accounts_page()
    page = AccountsPage(driver_login, driver_login.current_url)
    page.should_be_accounts_page()


def test_create_account(driver_login):
    page = AccountsPage(driver_login, driver_login.current_url)
    page.should_create_account_with_required_fields()

