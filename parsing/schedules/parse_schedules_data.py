from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from parsing.page_object import LoginPage
from parsing.page_object import ModeusPage

from selenium import webdriver
import pyautogui
from selenium.webdriver.chrome.options import Options
from work_with_db.schedules_table import *
import time


dates = [
    (2, "пн", "Понедельник"),
    (3, "вт", "Вторник"),
    (4, "ср", "Среда"),
    (5, "чт", "Четверг"),
    (6, "пт", "Пятница"),
    (7, "сб", "Суббота")
]


def open_new_tab(driver, link):
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    pyautogui.hotkey('ctrl', 't')

    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.close()

    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)


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
    modeus_page = ModeusPage(driver)
    modeus_page.go_to_modules_page()

    create_schedules_table(user_id=user_id)

    parsed_data = []

    # Modules parsing
    modules = modeus_page.get_modules()
    for module_index in range(len(modules)):
        modules = modeus_page.get_modules()
        module_link = modules[module_index]
        open_new_tab(driver, module_link)

        # Disciplines parsing
        disciplines_page_url = driver.current_url
        disciplines = modeus_page.get_disciplines()
        for discipline_index in range(len(disciplines)):
            disciplines = modeus_page.get_disciplines()
            discipline_name = disciplines[discipline_index].text  # <==
            discipline_xpath = f"//div[@class='item-name' and text()=' {discipline_name} ']"
            discipline_link = modeus_page.find_element_by_xpath(discipline_xpath)
            open_new_tab(driver, discipline_link)

            # Directions (schedules) parsing
            direction_buttons_xpath = ".//div[@class='item-name']/parent::div/parent::td/parent::tr[@class='item-row ng-star-inserted']"
            direction_buttons = modeus_page.find_elements_by_xpath(direction_buttons_xpath)
            for direction_button_index in range(len(direction_buttons)):
                direction_buttons = modeus_page.find_elements_by_xpath(direction_buttons_xpath)
                direction_name = direction_buttons[direction_button_index-1].text  # <==
                direction_link = direction_buttons[direction_button_index-1]
                open_new_tab(driver, direction_link)

                direction_schedule_page = driver.current_url

                direction_schedule_url = modeus_page.get_schedule_url()
                modeus_page.go_to(direction_schedule_url.get_attribute("href"))
                time.sleep(1)

                #
                for date in dates:
                    lessons_of_this_direction_xpath = f".//tbody//td[@class='fc-axis']/..//td[{date[0]}]//a"
                    lessons_of_this_direction = []
                    try:
                        lessons_of_this_direction = modeus_page.get_elems_by_custom_xpath(
                            lessons_of_this_direction_xpath)
                    except:
                        pass

                    for i in range(len(lessons_of_this_direction)):
                        info_located = False
                        while not info_located:
                            try:
                                next_direction_xpath = f"{lessons_of_this_direction_xpath}[{i + 1}]"
                                info = modeus_page.get_elem_by_custom_xpath(next_direction_xpath)
                                info.click()

                                popover = modeus_page.get_popover()
                                info_located = True

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

                                parsed_data.append([direction_name, lesson_type, weekday, lesson_time, teacher, team])

                            except Exception as ex:
                                # element_to_hover = modeus_page.get_h3_point()
                                # hover = ActionChains(driver).move_to_element(element_to_hover)
                                # hover.perform()
                                print(ex)
                #

                modeus_page.go_to(direction_schedule_page)

            modeus_page.go_to_disciplines_page(disciplines_page_url)

        modeus_page.go_to_modules_page()

    save_schedules_data_to_db(parsed_data, user_id=user_id)

    driver.close()
    return driver


start = time.perf_counter()

user_login = os.getenv('LOGIN')
user_password = os.getenv('PASSWORD')
user_id = "test"
create_and_fill_schedules_table(user_login, user_password, user_id)

stop = time.perf_counter()
print(f"Программа выполняется за {stop - start} секунд")

# Min: 262 сек
