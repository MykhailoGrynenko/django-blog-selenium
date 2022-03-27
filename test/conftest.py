import pytest
from faker import Faker

from src.locators import NewPostLocators
from src.page import RegisterPage, LoginPage, NewPost
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


@pytest.fixture(scope='session')
def driver():
    driver = DriverFactory.get_driver()
    driver.maximize_window()
    yield driver
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


@pytest.fixture(scope='session')
def login(driver, env_config, register):
    login_page = LoginPage(env_config, driver).open
    login_page.login_as(register[0], register[2])
    return login_page


@pytest.fixture(scope='session')
def create_post(driver, env_config, login):
    new_post = NewPost(env_config, driver).open
    new_post.create_post('post_title', 'post_content')
    return new_post
