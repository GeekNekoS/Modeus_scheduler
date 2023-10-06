from schedule_parsing.page_object import ModeusPage
import logging
import pytest
import time


LOGGER = logging.getLogger(__name__)


def test_copying_files(driver):
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
    modeus_main_page.click_math_module_schedule_button()

    LOGGER.info('OK')
    time.sleep(10)  # <==

    # LOGGER.info('The necessary folder for copying has been selected')
    # modeus_main_page.select_a_folder()
    #
    # LOGGER.info('Copied to the selected file')
    # modeus_main_page.click_copy()
    #
    # LOGGER.info('Double tap to open the file')
    # modeus_main_page.double_click_on_the_folder()
    #
    # LOGGER.info('Getting web elements of files to delete')
    # modeus_main_page.delete_files()
    #
    # expected_result = modeus_main_page.checking_the_expected_result()
    # assert len(expected_result) == 1
    # assert expected_result[0].get_attribute("aria-label") == "Файл для копирования.docx"
