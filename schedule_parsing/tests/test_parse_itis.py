from schedule_parsing.page_object import ModeusPage
import logging
import pytest
import time


LOGGER = logging.getLogger(__name__)


def test_parse_itis_1(driver):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(driver)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информатика для инженеров и исследователей (Онлайн, МИСИС, ОК)"')
    modeus_main_page.click_on_itis_1()

    LOGGER.info('Click on itis schedule "Информатика для инженеров и исследователей (Онлайн, МИСИС, ОК)"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(5)


def test_parse_itis_2(driver):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(driver)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы (онлайн, ИТМО, ОК)"')
    modeus_main_page.click_on_itis_2()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы (онлайн, ИТМО, ОК)"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(5)
