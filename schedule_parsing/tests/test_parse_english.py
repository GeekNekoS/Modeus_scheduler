from schedule_parsing.page_object import ModeusPage
import logging
import pytest
import time


LOGGER = logging.getLogger(__name__)
seconds = 1


def test_parse_english(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus English page opens')
    modeus_main_page.click_on_english_module()

    LOGGER.info('Click on English')
    modeus_main_page.click_on_english_lesson()

    LOGGER.info('Click on English level B2-C1')
    modeus_main_page.click_on_english_level_b2_c1()

    LOGGER.info('Click on English schedule button')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)
