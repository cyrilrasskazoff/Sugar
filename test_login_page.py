from .pages.login_page import LoginPage
from .pages.home_page import HomePage
from .pages.variables import URL


def test_admin_user_should_see_login_form_on_login_page(driver):
    url = URL
    page = LoginPage(driver, url)
    page.open()
    page.should_be_login_page()


def test_admin_user_is_navigated_to_home_page_after_login(driver):
    url = URL
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_home_page()
    home_page = HomePage(driver, url)
    home_page.should_be_home_page()

