import pytest

from selenium import webdriver

from src.config import Config


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
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
