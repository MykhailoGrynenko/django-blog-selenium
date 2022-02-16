import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (TimeoutException,
                                        InvalidElementStateException,
                                        )

from src.locators import NavigationLocators, LoginLocators


logging.basicConfig(filename='exceptions.log', level=logging.DEBUG)


class Page:
    url = 'https://myamazingdjangoblog.herokuapp.com'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)

    def find_element(self, element):
        try:
            elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(element)
            )
            return elem
        except TimeoutException:
            logging.warning(f'The element {element[1]} has not been found'
                            f'by the {element[0]} locator.')

    def click_on_element(self, element):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(element)
            ).click()
        except TimeoutException:
            logging.warning(f'The element {element[1]} has not been found'
                            f'by the {element[0]} locator.')

    def write(self, element, text):
        try:
            elem = self.find_element(element)
            elem.clear()
            elem.send_keys(text)
        except InvalidElementStateException:
            logging.warning(f'Cannot write to the element "{element[1]}"'
                            f' the text "{text}" by the "{element[0]}".')

    def is_displayed(self, element):
        return self.find_element(element)


class LoginPage(Page):
    @property
    def open(self):
        self.driver.get(f'{self.url}/login/')
        return self

    def login_as(self, username, password):
        self.write(LoginLocators.username, username)
        self.write(LoginLocators.pass_login, password)
        self.click_on_element(LoginLocators.button_login)

    def logout(self):
        self.click_on_element(NavigationLocators.logout)
