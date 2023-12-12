from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from work_with_db.schedules_table import *
from parsing.page_object import LoginPage
from parsing.page_object import ModeusPage
import pyautogui
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

                stop_if_data_more_then_170 = 0
                for date in dates:
                    lessons_of_this_direction_xpath = f".//tbody//td[@class='fc-axis']/..//td[{date[0]}]//a"
                    lessons_of_this_direction = []
                    try:
                        lessons_of_this_direction = modeus_page.get_elems_by_custom_xpath(
                            lessons_of_this_direction_xpath)
                    except:
                        pass

                    for lesson_index in range(len(lessons_of_this_direction)):
                        if stop_if_data_more_then_170 <= 170:
                            info_located = True
                            while info_located:
                                try:
                                    next_direction_xpath = f"{lessons_of_this_direction_xpath}[{lesson_index + 1}]"
                                    info = modeus_page.get_elem_by_custom_xpath(next_direction_xpath)

                                    lesson_time = info.text.split("\n")[0]
                                    if "https" in lesson_time:
                                        lesson_time = "Не определено"

                                    try:
                                        info.click()

                                        popover = modeus_page.get_popover()
                                        info_located = False

                                        data_from_popover = popover.text.split('\n')
                                        lesson_type = data_from_popover[2]
                                        weekday = date[2]
                                        teacher = data_from_popover[4].replace("\n", ", ")
                                        team = data_from_popover[3]

                                        element_to_hover = modeus_page.get_h3_point()
                                        hover = ActionChains(driver).move_to_element(element_to_hover)
                                        hover.perform()

                                        parsed_data.append([direction_name, lesson_type, weekday, lesson_time, teacher, team])
                                        stop_if_data_more_then_170 += 1
                                    except ElementClickInterceptedException as ex:
                                        info_located = False
                                        print(f" -> ElementClickInterceptedException: {ex}")

                                except TimeoutException as ex:
                                    print(f" -> TimeoutException: {ex}")

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

# Min:
# 1) 249 сек -> Neko's
# 2) 290 сек -> Innocent
