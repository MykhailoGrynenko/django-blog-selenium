""""
Module contains class, which creates single DriverFactory that provides specified WebDriver
"""

from selenium import webdriver


class DriverFactory:
    """"
    Class to create single DriverFactory that provides specified WebDriver
    """

    @staticmethod
    def get_driver(driver_name='firefox'):
        """
        Create driver according to given driver text name
        """
        if driver_name.lower() == 'chrome':
            _single_web_driver = webdriver.Chrome()
        elif driver_name.lower() == 'firefox':
            _single_web_driver = webdriver.Firefox()
        elif driver_name.lower() in ('ie', 'iexplorer', 'internetexplorer'):
            _single_web_driver = webdriver.Ie()
        elif driver_name.lower() == 'edge':
            _single_web_driver = webdriver.Edge()
        elif driver_name.lower() == 'safari':
            _single_web_driver = webdriver.Safari()
        elif driver_name.lower() == 'opera':
            _single_web_driver = webdriver.Opera()
        else:
            raise ValueError('Unknown name of browser')
        return _single_web_driver
