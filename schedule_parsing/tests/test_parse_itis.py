from schedule_parsing.page_object import ModeusPage
import logging
import pytest
import time


LOGGER = logging.getLogger(__name__)
seconds = 1


def test_parse_itis_1(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

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
    time.sleep(seconds)


def test_parse_itis_2(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

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
    time.sleep(seconds)


def test_parse_itis_3(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы (онлайн, УрФУ, ОК, ИНЖ)"')
    modeus_main_page.click_on_itis_3()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы (онлайн, УрФУ, ОК, ИНЖ)"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)


def test_parse_itis_4(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы (Смешанное, УрФУ, ОК). Мастерская Цифровые инструменты инженерного моделирования"')
    modeus_main_page.click_on_itis_4()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы (Смешанное, УрФУ, ОК). Мастерская Цифровые инструменты инженерного моделирования"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)


def test_parse_itis_5(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы (Смешанное, УрФУ, ОК). Мастерская Цифровые инструменты работы с документами"')
    modeus_main_page.click_on_itis_5()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы (Смешанное, УрФУ, ОК). Мастерская Цифровые инструменты работы с документами"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)


def test_parse_itis_6(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы (Смешанное, УрФУ, ОК). Мастерская Цифровые инструменты твердотельного 3D-моделирования"')
    modeus_main_page.click_on_itis_6()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы (Смешанное, УрФУ, ОК). Мастерская Цифровые инструменты твердотельного 3D-моделирования"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)


def test_parse_itis_7(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы. Цифровые инструменты визуализации данных"')
    modeus_main_page.click_on_itis_7()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы. Цифровые инструменты визуализации данных"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)


def test_parse_itis_8(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы. Цифровые инструменты исследовательской деятельности"')
    modeus_main_page.click_on_itis_8()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы. Цифровые инструменты исследовательской деятельности"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)


def test_parse_itis_9(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы. Цифровые инструменты моделирования для 3D-печати"')
    modeus_main_page.click_on_itis_9()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы. Цифровые инструменты моделирования для 3D-печати"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)


def test_parse_itis_10(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы. Цифровые инструменты обработки данных"')
    modeus_main_page.click_on_itis_10()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы. Цифровые инструменты обработки данных"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)


def test_parse_itis_11(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы. Цифровые инструменты полигонального 3D-моделирования"')
    modeus_main_page.click_on_itis_11()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы. Цифровые инструменты полигонального 3D-моделирования"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)


def test_parse_itis_12(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы. Цифровые инструменты проектирования игр"')
    modeus_main_page.click_on_itis_12()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы. Цифровые инструменты проектирования игр"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)


def test_parse_itis_13(login):
    # Authorization
    LOGGER.info('Precondition - authorization')
    modeus_main_page = ModeusPage(login)

    # Work on page
    LOGGER.info('The Modeus modules page opens')
    modeus_main_page.go_to_modules_page()

    LOGGER.info('The Modeus all lessons page opens')
    modeus_main_page.click_on_all_module()

    LOGGER.info('Click on itis lesson')
    modeus_main_page.click_on_itis_lesson()

    LOGGER.info('Click on itis module "Информационные технологии и сервисы. Цифровые инструменты проектирования умного дома"')
    modeus_main_page.click_on_itis_13()

    LOGGER.info('Click on itis schedule "Информационные технологии и сервисы. Цифровые инструменты проектирования умного дома"')
    modeus_main_page.click_on_lesson_module_button()

    LOGGER.info('Save data to DB')
    time.sleep(seconds)
