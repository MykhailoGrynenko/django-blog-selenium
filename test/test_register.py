import pytest

from src.page import RegisterPage


@pytest.mark.parametrize('email', ['', 'abc', '@mail.com' 'gns@', 'kek@com', 'dot@edu.'])
def test_register_invalid_email(email, driver, env_config, fake):
    fake_password = fake.password()
    register_page = RegisterPage(env_config, driver).open
    register_page.register_as(fake.user_name(), email, fake_password, fake_password)
    assert 'Enter a valid email address.' or 'Join Today' in driver.page_source
    assert "Your account has been created. You are now able to log in!" not in driver.page_source


@pytest.mark.parametrize('password', ['123', '124', '646464', '3647845678'])
def test_register_invalid_only_numeric_password(password, driver, env_config, fake):
    register_page = RegisterPage(env_config, driver).open
    register_page.register_as(fake.user_name(), fake.email(), password, password)
    assert 'This password is entirely numeric.' in driver.page_source
    assert "Your account has been created. You are now able to log in!" not in driver.page_source


@pytest.mark.parametrize('password', ['123456a', 'shorpas', 'a'])
def test_register_invalid_short_password(password, driver, env_config, fake):
    register_page = RegisterPage(env_config, driver).open
    register_page.register_as(fake.user_name(), fake.email(), password, password)
    assert 'This password is too short.' in driver.page_source
    assert "Your account has been created. You are now able to log in!" not in driver.page_source


@pytest.mark.parametrize('password', ['qwerty123', 'abcdefgh', 'password', 'testing1'])
def test_register_invalid_common_password(password, driver, env_config, fake):
    register_page = RegisterPage(env_config, driver).open
    register_page.register_as(fake.user_name(), fake.email(), password, password)
    assert 'This password is too common.' in driver.page_source
    assert "Your account has been created. You are now able to log in!" not in driver.page_source


@pytest.mark.parametrize('password', ['123', '124', '646464', '3647845678'])
def test_register_invalid_only_numeric_password(password, driver, env_config, fake):
    register_page = RegisterPage(env_config, driver).open
    register_page.register_as(fake.user_name(), fake.email(), password, password)
    assert 'This password is entirely numeric.' in driver.page_source
    assert "Your account has been created. You are now able to log in!" not in driver.page_source


def test_register_passwords_do_not_match(driver, env_config, fake):
    fake_password = fake.password()
    fake_password2 = fake_password + '_'
    register_page = RegisterPage(env_config, driver).open
    register_page.register_as(fake.user_name(), fake.email(), fake_password, fake_password2)
    assert "The two password fields didn’t match." in driver.page_source
    assert "Your account has been created. You are now able to log in!" not in driver.page_source


def test_register_valid_credentials(driver, env_config, fake):
    fake_password = fake.password()
    register_page = RegisterPage(env_config, driver).open
    register_page.register_as(fake.user_name(), fake.email(), fake_password, fake_password)
    assert 'Your account has been created. You are now able to log in!' in driver.page_source
