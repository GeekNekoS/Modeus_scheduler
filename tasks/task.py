from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from page_object_model.page_object import LoginPage
from page_object_model.page_object import ModeusPage
from selenium import webdriver
import pyautogui
import time
import os

from dotenv import load_dotenv
load_dotenv()


def parse():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    # login
    login_page.go_to_modules_page()
    login_page.enter_login(os.getenv('LOGIN'))
    login_page.enter_password(os.getenv('PASSWORD'))
    login_page.click_on_the_login_button()

    # Create and fill lessons table
    modeus_page = ModeusPage(driver)

    modules = modeus_page.get_modules()
    lessons = []
    modules_links = []
    for i in range(len(modules)):
        modules = modeus_page.get_modules()
        link = modules[i]
        ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        pyautogui.hotkey('ctrl', 't')

        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.close()

        window_after = driver.window_handles[0]
        driver.switch_to.window(window_after)

        module_url = driver.current_url
        modules_links.append(module_url)

        parsed_lessons = modeus_page.get_lessons()
        for lesson in parsed_lessons:
            lesson_name = lesson.text
            lessons.append(lesson_name)

            modeus_page.save_lesson_data_to_db(lesson_name, module_url)

        modeus_page.go_to_modules_page()

    driver.close()
    return driver


parse()
