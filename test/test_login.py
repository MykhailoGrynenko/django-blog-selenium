import os

from src.page import LoginPage
from src.locators import NavigationLocators


def test_login_invalid_credentials(driver):
    LoginPage(driver).open.login_as('incorrect_username',
                                    'incorrect_password')
    assert 'Please enter a correct username and password.'\
           in driver.page_source


def test_login_valid_credentials(driver):
    login_page = LoginPage(driver).open
    login_page.login_as(os.environ.get('DJANGO_USER'),
                        os.environ.get('DJANGO_PASS'))
    assert login_page.is_displayed(NavigationLocators.new_post)
    login_page.logout()
