from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from schedules_parsing.page_object import LoginPage
from schedules_parsing.page_object import ModeusPage
from selenium import webdriver
import pyautogui
from schedules_parsing.tasks.login import login

from dotenv import load_dotenv
load_dotenv()


def create_and_fill_lessons_table():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    # login
    login(login_page)

    # Create and fill lessons table
    modeus_page = ModeusPage(driver)

    modeus_page.create_lessons_table()

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


def main():
    create_and_fill_lessons_table()


if __name__ == "__main__":
    main()
