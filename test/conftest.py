import pytest
from faker import Faker

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
