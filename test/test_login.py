from src.page import LoginPage
from src.locators import NavigationLocators


def test_login_invalid_credentials(driver, env_config):
    LoginPage(env_config, driver).open.login_as('incorrect_username',
                                                'incorrect_password')
    assert 'Please enter a correct username and password.'\
           in driver.page_source


def test_login_valid_credentials(driver, env_config):
    login_page = LoginPage(env_config, driver).open
    login_page.login_as('TestUser22', 'qwerty54321')
    assert login_page.is_displayed(NavigationLocators.new_post)
    login_page.logout()
