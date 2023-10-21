from schedule_parsing.page_object import ModeusPage
import logging
import pytest
import time


LOGGER = logging.getLogger(__name__)
seconds = 1


def test_parse_russian_history(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_history_lesson()

    LOGGER.info('Click on itis module "История России (Смешанное, УГИ, СМУДС)"')
    modeus_main_page.click_on_russian_history()

    LOGGER.info('Click on itis schedule "История России (Смешанное, УГИ, СМУДС)"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)


def test_parse_history_of_russian_civilization(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_history_lesson()

    LOGGER.info('Click on itis module "История российской цивилизации (Смешанное, ЦРУК, ОНЛАЙН НТК)"')
    modeus_main_page.click_on_history_of_russian_civilization()

    LOGGER.info('Click on itis schedule "История российской цивилизации (Смешанное, ЦРУК, ОНЛАЙН НТК)"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)
