import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from .pages.variables import URL
from .pages.login_page import LoginPage
from .pages.home_page import HomePage


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="firefox",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        # options.add_argument("--window-size=1440,900")
        # options.add_argument("start-maximized")
        # options.add_argument("headless")
        options.add_argument("start-fullscreen")
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_firefox = OptionsFirefox()
        # options_firefox.add_argument("headless")
        options_firefox.add_argument("start-fullscreen")
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(options=options_firefox, service=service)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.fixture(scope="module")
def driver_login(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        # options.add_argument("--window-size=1440,900")
        # options.add_argument("start-maximized")
        # options.add_argument("headless")
        options.add_argument("start-fullscreen")
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_firefox = OptionsFirefox()
        # options_firefox.add_argument("headless")
        options_firefox.add_argument("start-fullscreen")
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(options=options_firefox, service=service)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    url = URL
    page = LoginPage(driver, url)
    page.open()
    page.login_admin_and_navigate_to_home_page()
    home_page = HomePage(driver, driver.current_url)
    home_page.should_be_home_page()
    yield driver
    print("\nquit browser..")
    driver.quit()
