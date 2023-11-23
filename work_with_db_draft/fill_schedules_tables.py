import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import psycopg2

from dotenv import load_dotenv
load_dotenv()


def parse():
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)

    def get_connect(url, retry=3):
        """Prevents from possible connection breaks"""
        try:
            driver.get(url=url)
        except Exception as exception:
            if retry:
                print(f"\033[38;5;{196}mReconnecting\033[0;0m")
                print(exception)
                return get_connect(url, retry=(retry - 1))
            else:
                raise
        else:
            return driver.get(url=url)

    url = 'https://urfu.modeus.org/learning-path-selection/menus'

    driver.maximize_window()

    get_connect(url)
    time.sleep(2)

    # Login
    login = driver.find_element(By.XPATH, "//input[@placeholder='proverka@example.com']")
    login.send_keys(os.getenv('LOGIN'))
    time.sleep(1)
    #
    password = driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
    password.send_keys(os.getenv('PASSWORD'))
    time.sleep(1)
    #
    login_button = driver.find_element(By.XPATH, "//span[@class='submit']")
    login_button.click()
    time.sleep(1)

    # Schedules
    directions_info = None
    try:
        with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM directions"""
            cursor.execute(query)
            directions_info = cursor.fetchall()
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")

    for direction in directions_info:
        direction_url = direction[2]
        get_connect(direction_url)
        time.sleep(3)

        try:
            with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    CREATE TABLE schedules (
                        id SERIAL PRIMARY KEY,
                        lesson_name VARCHAR,
                        lesson_type VARCHAR,
                        weekday VARCHAR, 
                        lesson_time VARCHAR,
                        teacher VARCHAR,
                        place VARCHAR,
                        team VARCHAR
                    );
                """)
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

        for date in [(2, "пн", "Понедельник"), (3, "вт", "Вторник"), (4, "ср", "Среда"), (5, "чт", "Четверг"), (6, "пт", "Пятница"), (7, "сб", "Суббота")]:
            lessons_of_this_direction_xpath = f".//tbody//td[@class='fc-axis']/..//td[{date[0]}]//a"
            lessons_of_this_direction = driver.find_elements(By.XPATH, lessons_of_this_direction_xpath)

            for i in range(len(lessons_of_this_direction)):
                info = driver.find_element(By.XPATH, f"{lessons_of_this_direction_xpath}[{i+1}]")
                info.click()
                popover = driver.find_element(By.XPATH, "//ngb-popover-window")
                time.sleep(1)

                lessons_data = driver.find_element(By.XPATH, f"{lessons_of_this_direction_xpath}[{i+1}]//div[@class='fc-title']").text.split(" / ")
                try:
                    lesson_name, lesson_type = lessons_data[0], lessons_data[1]
                except:
                    lesson_name, lesson_type = lessons_data[0], "Не указано"
                weekday = date[2]
                lesson_time = driver.find_element(By.XPATH, f"{lessons_of_this_direction_xpath}[{i+1}]//div[@class='fc-time']/span").text
                teacher = driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']").text
                place = "Аудитория не определена"
                try:
                    place = driver.find_element(By.XPATH, f"{lessons_of_this_direction_xpath}[{i+1}]//div[@class='fc-time']/small").text.split(" / ")[1]
                except:
                    pass
                team = popover.text.split("\n")[3].replace(f"{lesson_name} ", "")  # <==

                element_to_hover_over = driver.find_element(By.XPATH, "//h3[text()='Мое расписание']")
                hover = ActionChains(driver).move_to_element(element_to_hover_over)
                hover.perform()

                try:
                    with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
                        cursor = connection.cursor()

                        cursor.execute("""
                            INSERT INTO schedules (
                                lesson_name, 
                                lesson_type, 
                                weekday, 
                                lesson_time, 
                                teacher,
                                place,
                                team
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """, (
                            lesson_name,
                            lesson_type,
                            weekday,
                            lesson_time,
                            teacher,
                            place,
                            team
                        )
                                       )
                except Exception as ex:
                    print(f"Can`t establish connection to database: {ex}\n")

    driver.close()
    return driver


def main():
    parse()


if __name__ == "__main__":
    main()
