import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


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
