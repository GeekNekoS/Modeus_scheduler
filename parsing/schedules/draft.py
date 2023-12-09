from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from parsing.page_object import LoginPage
from parsing.page_object import ModulesPages
from parsing.page_object import ModeusPage

from selenium import webdriver
import pyautogui
from selenium.webdriver.chrome.options import Options
import time
import os

from dotenv import load_dotenv
load_dotenv()


def create_and_fill_schedules_table(user_login, user_password, user_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome()  # options=chrome_options
    driver.maximize_window()

    # login
    login_page = LoginPage(driver)
    login_page.go_to_modules_page()
    login_page.enter_login(user_login)
    login_page.enter_password(user_password)
    login_page.click_on_the_login_button()

    # Create and fill lessons table
    modules_page = ModulesPages(driver)
    modules_page.go_to_modules_page()

    modeus_page = ModulesPages(driver)

    modules_page.create_schedules_table(user_id=user_id)

    parsed_data = []

    discipline_names = []
    direction_names = []
    disciplines_page_urls = []

    # Modules parsing
    modules = modeus_page.get_modules()
    for i in range(len(modules)):
        modules = modeus_page.get_modules()
        module_name = modules[i].text  # <==
        module_link = modules[i]
        ActionChains(driver).key_down(Keys.CONTROL).click(module_link).key_up(Keys.CONTROL).perform()
        pyautogui.hotkey('ctrl', 't')

        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.close()

        window_after = driver.window_handles[0]
        driver.switch_to.window(window_after)

        # Disciplines parsing
        disciplines_page_url = driver.current_url
        disciplines_page_urls.append(disciplines_page_url)
        disciplines = modeus_page.get_disciplines()
        for i in range(len(disciplines)):
            disciplines = modeus_page.get_disciplines()
            discipline_name = disciplines[i].text  # <==
            discipline_names.append(discipline_name)
            discipline_xpath = f"//div[@class='item-name' and text()=' {discipline_name} ']"

            discipline_link = modeus_page.find_element_by_xpath(discipline_xpath)

            ActionChains(driver).key_down(Keys.CONTROL).click(discipline_link).key_up(Keys.CONTROL).perform()
            pyautogui.hotkey('ctrl', 't')

            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            driver.close()

            window_after = driver.window_handles[0]
            driver.switch_to.window(window_after)

            # Directions parsing
            directions = modeus_page.get_directions()
            for i in range(len(directions)):
                directions = modeus_page.get_directions()
                direction_name = directions[i].text
                direction_names.append(direction_name)

            # Schedules parsing
            direction_buttons_xpath = ".//div[@class='item-name']/parent::div/parent::td/parent::tr[@class='item-row ng-star-inserted']"
            direction_buttons = modeus_page.find_elements_by_xpath(direction_buttons_xpath)
            for i in range(len(direction_buttons)):
                direction_buttons = modeus_page.find_elements_by_xpath(direction_buttons_xpath)
                direction_name = direction_buttons[i-1].text  # <==
                direction_link = direction_buttons[i-1]

                ActionChains(driver).key_down(Keys.CONTROL).click(direction_link).key_up(Keys.CONTROL).perform()
                pyautogui.hotkey('ctrl', 't')

                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                driver.close()

                window_after = driver.window_handles[0]
                driver.switch_to.window(window_after)

                direction_schedule_page = driver.current_url

                direction_schedule_url = modeus_page.get_schedule_url()
                modules_page.go_to(direction_schedule_url.get_attribute("href"))
                time.sleep(1)

                #
                dates = [
                    (2, "пн", "Понедельник"),
                    (3, "вт", "Вторник"),
                    (4, "ср", "Среда"),
                    (5, "чт", "Четверг"),
                    (6, "пт", "Пятница"),
                    (7, "сб", "Суббота")
                ]

                for date in dates:
                    lessons_of_this_direction_xpath = f".//tbody//td[@class='fc-axis']/..//td[{date[0]}]//a"
                    lessons_of_this_direction = []
                    try:
                        lessons_of_this_direction = modeus_page.get_elems_by_custom_xpath(
                            lessons_of_this_direction_xpath)
                    except:
                        pass

                    for i in range(len(lessons_of_this_direction)):
                        next_direction_xpath = f"{lessons_of_this_direction_xpath}[{i + 1}]"
                        info = modeus_page.get_elem_by_custom_xpath(next_direction_xpath)
                        info.click()

                        popover = None
                        try:
                            popover = modeus_page.get_popover()
                        except:
                            popover = modeus_page.get_popover()

                        lessons_data_xpath = f"{lessons_of_this_direction_xpath}[{i + 1}]//div[@class='fc-title']"
                        lessons_data = modeus_page.get_elem_by_custom_xpath(lessons_data_xpath).text.split(" / ")
                        try:
                            lesson_name, lesson_type = lessons_data[0], lessons_data[1]
                        except:
                            lesson_name, lesson_type = lessons_data[0], "Не указано"
                        weekday = date[2]
                        lesson_time_xpath = f"{lessons_of_this_direction_xpath}[{i + 1}]//div[@class='fc-time']/span"
                        lesson_time = modeus_page.get_elem_by_custom_xpath(lesson_time_xpath).text
                        teacher = modeus_page.get_teachers_name()
                        team = popover.text.split("\n")[3].replace(f"{lesson_name} ", "")

                        element_to_hover = modeus_page.get_h3_point()
                        hover = ActionChains(driver).move_to_element(element_to_hover)
                        hover.perform()

                        # -=-= Test saving =-=-
                        # modules_page.save_schadules_data_to_db(module_name, discipline_name, direction_name, lesson_name, lesson_type, weekday, lesson_time, teacher, team, user_id=user_id)
                        parsed_data.append([module_name, discipline_name, direction_name, lesson_name, lesson_type, weekday, lesson_time, teacher, team])
                        # -=-=-=-=-=-=-=-=-=-=-
                #

                modules_page.go_to(direction_schedule_page)

            modeus_page.go_to_disciplines_page(disciplines_page_url)

        modeus_page.go_to_modules_page()

    modules_page.save_schadules_data_to_db(parsed_data)

    # -=-= Test saving =-=-
    # for data in parsed_data:
    #     print(data)
    # -=-=-=-=-=-=-=-=-=-=-

    driver.close()
    return driver


# start = time.perf_counter()
#
# user_login = os.getenv('LOGIN')
# user_password = os.getenv('PASSWORD')
# user_id = "test"
# create_and_fill_schedules_table(user_login, user_password, user_id)
#
# stop = time.perf_counter()
# print(f"Программа выполняется за {stop - start} секунд")

# С записью каждого направления по отдельности: 278
# Отдельно парсинг: 262
# С одноразовой поставкой данных в базу:
