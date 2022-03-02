import pytest
import allure
from allure_commons.types import AttachmentType
from faker import Faker

from src.page import RegisterPage, LoginPage
from src.config import Config
from src.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption('--env',
                     action='store',
                     default='dev',
                     help='Environment to run tests.')


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption('--env')


@pytest.fixture(scope='session')
def env_config(env):
    return Config(env)


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
    # if rep.failed:
    #     if rep.when == "setup":
    #         print("Setup failed!WWWWWWWWWWWWW")
    #     elif rep.when == "call":
    #         print("Test method failedOOOOOOOOOOOOO")
    # elif rep.passed and rep.when == "call":
    #     print('passedddddd')


@pytest.fixture(scope='session')
def driver(request):
    driver = DriverFactory.get_driver()
    driver.maximize_window()
    yield driver
    # attach = driver.get_screenshot_as_png()
    # allure.attach(request.function.__name__, attach, attachment_type=AttachmentType.PNG)
    # allure.attach('screenshot', attach, allure.attach_type.PNG)
    # if request.node.rep_setup.failed:
    #     allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
    # elif request.node.rep_setup.passed:
    #     if request.node.rep_call.failed:
    #         allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
    driver.quit()


@pytest.fixture(scope='session')
def fake():
    return Faker()


@pytest.fixture(scope='session')
def register(driver, env_config, fake):
    fake_username = fake.user_name()
    fake_email = fake.email()
    fake_password = fake.password()
    register_page = RegisterPage(env_config, driver).open
    register_page.register_as(fake_username, fake_email, fake_password, fake_password)
    return fake_username, fake_email, fake_password


# @allure.step('initiation login')
@pytest.fixture(scope='session')
def login(driver, env_config, register):
    login_page = LoginPage(env_config, driver).open
    login_page.login_as(register[0], register[2])
    return login_page
