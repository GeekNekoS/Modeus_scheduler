from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from parsing.page_object import LoginPage
from parsing.page_object import ModeusPage
from selenium import webdriver
import pyautogui
from parsing.schedules.login import login
from selenium.webdriver.chrome.options import Options
import time

from dotenv import load_dotenv
load_dotenv()


def create_and_fill_schedules_table():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    login_page = LoginPage(driver)

    # login
    login(login_page)

    # Create and fill lessons table
    modeus_page = ModeusPage(driver)
    # modeus_page.go_to_modules_page()

    directions_info = modeus_page.get_directions_from_db()

    dates = [
        (2, "пн", "Понедельник"),
        (3, "вт", "Вторник"),
        (4, "ср", "Среда"),
        (5, "чт", "Четверг"),
        (6, "пт", "Пятница"),
        (7, "сб", "Суббота")
    ]

    for direction in directions_info:
        direction_url = direction[2]
        modeus_page.get_connect(direction_url)

        modeus_page.create_schedules_table()

        for date in dates:
            lessons_of_this_direction_xpath = f".//tbody//td[@class='fc-axis']/..//td[{date[0]}]//a"
            lessons_of_this_direction = []
            try:
                lessons_of_this_direction = modeus_page.get_elems_by_custom_xpath(lessons_of_this_direction_xpath)
            except:
                pass
            print(lessons_of_this_direction)

            for i in range(len(lessons_of_this_direction)):
                next_direction_xpath = f"{lessons_of_this_direction_xpath}[{i+1}]"
                info = modeus_page.get_elem_by_custom_xpath(next_direction_xpath)
                info.click()

                popover = None
                try:
                    popover = modeus_page.get_popover()
                except:
                    popover = modeus_page.get_popover()
                # time.sleep(1)

                lessons_data_xpath = f"{lessons_of_this_direction_xpath}[{i+1}]//div[@class='fc-title']"
                lessons_data = modeus_page.get_elem_by_custom_xpath(lessons_data_xpath).text.split(" / ")
                try:
                    lesson_name, lesson_type = lessons_data[0], lessons_data[1]
                except:
                    lesson_name, lesson_type = lessons_data[0], "Не указано"
                weekday = date[2]
                lesson_time_xpath = f"{lessons_of_this_direction_xpath}[{i + 1}]//div[@class='fc-time']/span"
                lesson_time = modeus_page.get_elem_by_custom_xpath(lesson_time_xpath).text
                teacher = modeus_page.get_teachers_name()
                try:
                    place_xpath = f"{lessons_of_this_direction_xpath}[{i + 1}]//div[@class='fc-time']/small"
                    place = modeus_page.get_elem_by_custom_xpath(place_xpath).text.split(" / ")[1]
                except:
                    place = "Аудитория не определена"
                team = popover.text.split("\n")[3].replace(f"{lesson_name} ", "")

                element_to_hover = modeus_page.get_h3_point()
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                modeus_page.save_schedules_data_to_db(lesson_name, lesson_type, weekday, lesson_time, teacher, place, team)

    driver.close()
    return driver


def main():
    create_and_fill_schedules_table()


if __name__ == "__main__":
    main()
