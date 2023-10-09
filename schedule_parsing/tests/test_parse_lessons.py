from schedule_parsing.page_object import ModeusPage
import logging
import pytest
import time


LOGGER = logging.getLogger(__name__)


def test_math_basic(driver):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(driver)

    # Work on page
    LOGGER.info('The Modeus page opens')
    modeus_main_page.go_to_lessons_page()

    LOGGER.info('Click on math lesson')
    modeus_main_page.click_math_button()

    LOGGER.info('Click on the math basic level button')
    modeus_main_page.click_math_basic_level_button()

    LOGGER.info('Click on the "copy" method')
    modeus_main_page.click_on_module_math_basic_level_button()

    LOGGER.info('OK')
    time.sleep(10)


def itis():
    pass
