import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (TimeoutException,
                                        InvalidElementStateException,
                                        )

from src.locators import NavigationLocators, LoginLocators, RegisterLocators, NewPostLocators


logging.basicConfig(filename='exceptions.log', level=logging.DEBUG)


class Page:

    def __init__(self, env_config, driver):
        self.driver = driver
        self.env_config = env_config
        self.driver.get(self.env_config.base_url)

    def find_element(self, element):
        try:
            elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(element)
            )
            logging.info(f'The element with locator {element[1]} by type: '
                         f'{element[0]} found!')
            return elem
        except TimeoutException:
            logging.warning(f'The element {element[1]} has not been found '
                            f'by the {element[0]} locator.')
        except Exception as e:
            logging.warning(e)

    def click_on_element(self, element):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(element)
            ).click()
            logging.info(f'The element with locator {element[1]} by type: '
                         f'{element[0]} has been clicked!')
        except TimeoutException:
            logging.warning(f'The element {element[1]} has not been found '
                            f'by the {element[0]} locator.')
        except Exception as e:
            logging.warning(e)

    def write(self, element, text):
        try:
            elem = self.find_element(element)
            elem.clear()
            elem.send_keys(text)
            logging.info(f'Write to the element "{element[1]}" '
                         f' the text "{text}" by the "{element[0]}".')
        except InvalidElementStateException:
            logging.warning(f'Cannot write to the element "{element[1]}" '
                            f' the text "{text}" by the "{element[0]}".')
        except Exception as e:
            logging.warning(e)

    def get_element_text(self, element):
        return self.find_element(element).text

    def get_input_text(self, element):
        return self.find_element(element).get_attribute('value')

    def is_displayed(self, element):
        return self.find_element(element)


class LoginPage(Page):
    @property
    def open(self):
        self.driver.get(f'{self.env_config.base_url}/login/')
        return self

    def login_as(self, username, password):
        self.write(LoginLocators.username, username)
        self.write(LoginLocators.pass_login, password)
        self.click_on_element(LoginLocators.button_login)

    def logout(self):
        self.click_on_element(NavigationLocators.logout)


class RegisterPage(Page):
    @property
    def open(self):
        self.driver.get(f'{self.env_config.base_url}/register/')
        return self

    def register_as(self, username, email, password, password_confirm):
        self.write(RegisterLocators.username, username)
        self.write(RegisterLocators.email, email)
        self.write(RegisterLocators.pass_register_one, password)
        self.write(RegisterLocators.pass_register_two, password_confirm)
        self.click_on_element(RegisterLocators.button_sign_up)


class NewPost(Page):
    @property
    def open(self):
        self.driver.get(f'{self.env_config.base_url}/post/new/')
        return self

    def create_post(self, title, content):
        self.write(NewPostLocators.create_title, title)
        self.write(NewPostLocators.crate_content, content)
        self.click_on_element(NewPostLocators.button_post)

    def update_post(self, title=None, content=None):
        self.click_on_element(NewPostLocators.button_update)
        if title:
            self.write(NewPostLocators.update_title, title)
        if content:
            self.write(NewPostLocators.update_content, content)
        self.click_on_element(NewPostLocators.button_update_confirm)

    def delete_post(self):
        self.click_on_element(NewPostLocators.button_delete)
        self.click_on_element(NewPostLocators.button_yes_delete)
