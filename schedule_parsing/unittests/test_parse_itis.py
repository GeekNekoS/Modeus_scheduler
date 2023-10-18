from schedule_parsing.page_object import LoginPage
from schedule_parsing.page_object import ModeusPage
from dotenv import load_dotenv
from selenium import webdriver
import unittest
import logging
import time
import os


LOGGER = logging.getLogger(__name__)
load_dotenv()


class ParseItis(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        LOGGER.info('The browser opens on the main page')
        modeus_main_page = LoginPage(self.driver)

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

        # Authorization
        LOGGER.info('Precondition - authorization')
        self.modeus_main_page = ModeusPage(self.driver)

        # Work on page
        LOGGER.info('The Modeus modules page opens')
        self.modeus_main_page.go_to_modules_page()

        LOGGER.info('The Modeus all lessons page opens')
        self.modeus_main_page.click_on_all_module()

        LOGGER.info('Click on itis lesson')
        self.modeus_main_page.click_on_itis_lesson()

        LOGGER.info('Click on itis module "Информатика для инженеров и исследователей (Онлайн, МИСИС, ОК)"')
        self.modeus_main_page.click_on_itis_1()

    def test_parse_itis_1(self):
        LOGGER.info('Click on itis module "Информатика для инженеров и исследователей (Онлайн, МИСИС, ОК)"')
        self.modeus_main_page.click_on_itis_1()

    def test_parse_itis_2(self):
        LOGGER.info('Click on itis module "Информационные технологии и сервисы (онлайн, ИТМО, ОК)"')
        self.modeus_main_page.click_on_itis_2()

    def test_parse_itis_3(self):
        LOGGER.info('Click on itis module "Информационные технологии и сервисы (онлайн, УрФУ, ОК, ИНЖ)"')
        self.modeus_main_page.click_on_itis_3()

    def tearDown(self):
        LOGGER.info('Click on itis schedule "Информатика для инженеров и исследователей (Онлайн, МИСИС, ОК)"')
        self.modeus_main_page.click_on_lesson_module_button()

        LOGGER.info('Save data to DB')
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
