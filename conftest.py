import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging.config
from log_settings import LOGGING_CONFIG

from src.app.application import Application
from src.app.page_factory import Pages
from src.models.auth import AuthData
from src.pages.auth_page import AuthPage
from src.pages.user_page import UseDiskPage

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("tz_ui")


@pytest.fixture(scope="session")
def app(request):
    headless_mode = str.lower(request.config.getoption("--headless"))
    # app_host = request.config.getoption("--app-host")
    # app_port = request.config.getoption("--app-port")
    app_url = request.config.getoption("--app-url")
    web_driver_manager = request.config.getoption("--webdr-manager")
    web_driver_path = request.config.getoption("--webdr-path")

    logger.info(f"Старт http://{app_url} режим headless={headless_mode} mode")

    chrome_options = None

    if headless_mode == "true":
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.headless = True

    elif headless_mode != "false":
        raise pytest.UsageError("--headless опция должна быть true или false")

    is_manager = False
    if web_driver_manager == "true":
        is_manager = True

    app = Application(
        driver=get_webdriver(is_manager=is_manager, options=chrome_options, web_driver_path=web_driver_path),
        app_url=app_url
    )

    yield app
    app.quit()


def get_webdriver(is_manager=True, web_driver_path=None, options=None):
    if is_manager:
        return webdriver.Chrome(ChromeDriverManager().install(), options=options)
    else:
        return webdriver.Chrome(service=Service(executable_path=web_driver_path), options=options)


@pytest.fixture(scope="session")
def auth(app, request):
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    auth_page: AuthPage = app.get_page(Pages.AUTH_PAGE)
    auth_page.open()
    auth_page.auth(AuthData(login=user, password=password))
    yield
    # app.user_menu.sign_out()


@pytest.fixture
def user_disk_page(app, auth):
    """Передает страницу клиента Яндекс.Диск."""
    user_disk_page: UseDiskPage = app.get_page(Pages.USER_DISK_PAGE)
    yield user_disk_page
    user_disk_page.logout()


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
             "enter 'false' - if not",
    ),
    parser.addoption(
        "--app-url",
        action="store",
        default="https://disk.yandex.ru",
        help="enter application url",
    ),
    parser.addoption(
        "--webdr-manager",
        action="store",
        default="true",
        help="enter 'true' if you want run tests with selenium webdriver manager,\n"
             "enter 'false' - if not",
    ),
    parser.addoption(
        "--webdr-path",
        action="store",
        default="C:\\Program Files\\chromedriver\\chromedriver",
        help="enter selenium chrome web driver path",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="o.bortnikova22",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="oB22tz*",
        help="enter password",
    ),


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if "app" in item.fixturenames:
                web_driver = item.funcargs["app"]
            else:
                logger.error("Fail to take screen-shot")
                return
            logger.info("Screen-shot done")
            allure.attach(
                web_driver.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            logger.error("Fail to take screen-shot: {}".format(e))
