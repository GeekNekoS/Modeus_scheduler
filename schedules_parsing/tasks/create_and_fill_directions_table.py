from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from schedules_parsing.page_object import LoginPage
from schedules_parsing.page_object import ModeusPage
from selenium import webdriver
import pyautogui
from schedules_parsing.tasks.login import login

from dotenv import load_dotenv
load_dotenv()


def create_and_fill_directions_table():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    # login
    login(login_page)

    # Create and fill directions table
    modeus_page = ModeusPage(driver)

    modeus_page.create_directions_table()

    lessons_info = modeus_page.get_lessons_data()

    remove_this = []
    for lesson in lessons_info:
        remove_this.append(lesson[1])

    for lesson in lessons_info:
        modeus_page.get_connect(lesson[2])
        lesson_id = lesson[0]

        modeus_page.click_on_direction_name(lesson[1])

        directions = modeus_page.get_directions()

        directions_of_module = []
        for direction in directions:
            direction_name = direction.text
            if direction_name not in remove_this:
                directions_of_module.append(direction_name)

        for direction_name in directions_of_module:
            direction_button = modeus_page.get_direction_button(direction_name)

            ActionChains(driver).key_down(Keys.CONTROL).click(direction_button).key_up(Keys.CONTROL).perform()
            pyautogui.hotkey('ctrl', 't')

            go_to = driver.current_url

            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)

            modeus_page.get_connect(go_to)

            direction_url = modeus_page.get_direction_url()

            driver.close()

            window_after = driver.window_handles[0]
            driver.switch_to.window(window_after)

            modeus_page.save_directions_data_to_db(direction_name, direction_url, lesson_id)

    driver.close()
    return driver


create_and_fill_directions_table()
