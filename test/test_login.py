import os
import allure

from src.page import LoginPage
from src.locators import NavigationLocators, LoginLocators


@allure.step("don't know what's happening - ")
def test_login_invalid_credentials(driver, env_config):
    login_page = LoginPage(env_config, driver).open
    login_page.login_as('incorrect_username', 'incorrect_password')
    assert 'Please enter a correct username and password.' \
           in login_page.find_element(LoginLocators.incorrect_data).text


@allure.step
def test_login_valid_credentials(driver, env_config):
    login_page = LoginPage(env_config, driver).open
    login_page.login_as(os.environ.get('DJANGO_USER'),
                        os.environ.get('DJANGO_PASS'))
    assert login_page.is_displayed(NavigationLocators.new_post)
    login_page.logout()
