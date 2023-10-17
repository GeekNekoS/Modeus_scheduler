from schedule_parsing.page_object import LoginPage
from dotenv import load_dotenv
from selenium import webdriver
import unittest
import logging
import time
import os


LOGGER = logging.getLogger(__name__)
load_dotenv()


class TestUM(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()

        LOGGER.info('The browser opens on the main page')
        modeus_main_page = LoginPage(driver)

        LOGGER.info('The auth page opens')
        modeus_main_page.go_to_auth_page()

        LOGGER.info('Login entered')
        modeus_main_page.enter_login(os.getenv('LOGIN'))

        LOGGER.info('Password entered')
        modeus_main_page.enter_password(os.getenv('PASSWORD'))

        LOGGER.info('The login button is pressed')
        modeus_main_page.click_on_the_login_button()

        LOGGER.info('Authorization upload')
        time.sleep(3)

    def test_numbers_3_4(self):
        self.assertEqual(3 * 4, 12)

    def test_strings_a_3(self):
        self.assertEqual('a' * 3, 'aaa')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
