from parsing.locators import *
from parsing.base_page import BaseClass
import psycopg2
from selenium.common.exceptions import TimeoutException as TE
import os

from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')  # DATABASE_URL


class LoginPage(BaseClass):
    # Log in
    def enter_login(self, login):
        return self.find_element(LoginLocators.LOGIN_INPUT, time=self.time).send_keys(login)

    def enter_password(self, password):
        return self.find_element(LoginLocators.PASSWORD_INPUT, time=self.time).send_keys(password)

    def click_on_the_login_button(self):
        return self.find_element(LoginLocators.LOGIN_BUTTON, time=self.time).click()

    def check_logedin(self):
        flag = False
        try:
            rus_warning = self.find_element(LoginLocators.RUS_WARNING, time=self.time)
        except:
            try:
                eng_warning = self.find_element(LoginLocators.ENG_WARNING, time=self.time)
            except:
                flag = True

        return flag

    # Log out


class ModeusPage(BaseClass):
    def create_lessons_table(self, user_id=None):
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""
                    CREATE TABLE lessons_{user_id} (
                        id SERIAL PRIMARY KEY,
                        lesson VARCHAR,
                        module_url VARCHAR
                    );
                """)
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

    def get_modules(self):
        return self.find_elements(ModeusLocators.MODULES, time=self.time)

    def get_lessons(self):
        return self.find_elements(ModeusLocators.LESSONS, time=self.time)

    def save_lesson_data_to_db(self, *data, user_id=None):
        lesson_name, module_url = data
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()

                cursor.execute(f"""
                    INSERT INTO lessons_{user_id} (lesson, module_url) VALUES (%s, %s)
                    """, (lesson_name, module_url)
                               )
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

    def create_directions_table(self, user_id=None):
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""
                    CREATE TABLE directions_{user_id} (
                        id SERIAL PRIMARY KEY,
                        direction VARCHAR,
                        schedule_url VARCHAR,
                        foreign_key INT
                    );
                """)
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

    def get_lessons_data(self, user_id=None):
        lessons_info = None
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()
                query = f"""SELECT * FROM lessons_{user_id}"""
                cursor.execute(query)
                lessons_info = cursor.fetchall()
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")
        return lessons_info

    def click_on_direction_name(self, direction_name):
        return self.find_element((By.XPATH, f"//div[@class='item-name' and text()=' {direction_name} ']"), time=self.time).click()

    def get_directions(self):
        return self.find_elements(ModeusLocators.DIRECTIONS, time=self.time)[1:]

    def get_direction_button(self, direction_name):
        return self.find_element((By.XPATH, f"//div[@class='item-name' and text()=' {direction_name} ']"), time=self.time)

    def get_direction_url(self):
        direction_schedule_button = self.find_element(ModeusLocators.DIRECTION_SCHEDULE_BUTTON, time=self.time)
        return direction_schedule_button.get_attribute("href")

    def save_directions_data_to_db(self, *data, user_id=None):
        direction_name, direction_url, lesson_id = data
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()

                cursor.execute(f"""
                    INSERT INTO directions_{user_id} (direction, schedule_url, foreign_key) VALUES (%s, %s, %s)
                    """, (direction_name, direction_url, lesson_id)
                               )
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

    def get_directions_from_db(self, user_id=None):
        directions_info = None
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()
                query = f"""SELECT * FROM directions_{user_id}"""
                cursor.execute(query)
                directions_info = cursor.fetchall()
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")
        return directions_info

    def create_schedules_table(self, user_id=None):
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""
                    CREATE TABLE schedules_{user_id} (
                        lesson_name VARCHAR,
                        direction_name VARCHAR,
                        lesson_type VARCHAR,
                        weekday VARCHAR, 
                        lesson_time VARCHAR,
                        teacher VARCHAR,
                        team VARCHAR
                    );
                """)
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

    def get_popover(self):
        return self.find_element(ModeusLocators.POPOVER, time=self.time)

    def get_teachers_name(self):
        return self.find_element(ModeusLocators.TEACHERS_NAME, time=self.time).text

    def get_h3_point(self):
        return self.find_element(ModeusLocators.H3_MY_SCHEDULE, time=self.time)

    def save_schedules_data_to_db(self, *data, user_id=None):
        lesson_name, direction_name, lesson_type, weekday, lesson_time, teacher, team = data
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()

                cursor.execute(f"""
                    INSERT INTO schedules_{user_id} (lesson_name, direction_name, lesson_type, weekday, lesson_time, teacher, team) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (lesson_name, direction_name, lesson_type, weekday, lesson_time, teacher, team)
                    )
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")


class ModulesPages(BaseClass):
    def get_modules(self):
        return self.find_elements(ModeusLocators.MODULES, time=self.time)

    def get_disciplines(self):
        return self.find_elements(ModeusLocators.DISCIPLINES, time=self.time)

    def get_directions(self):
        return self.find_elements(ModeusLocators.DIRECTIONS, time=self.time)

    def find_element_by_xpath(self, xpath):
        return self.find_element((By.XPATH, xpath), time=self.time)

    def find_elements_by_xpath(self, xpath):
        return self.find_elements((By.XPATH, xpath), time=self.time)

    def go_to_disciplines_page(self, disciplines_page_url):
        return self.get_connect(disciplines_page_url)

    def create_schedules_table(self, user_id=None):
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""
                    CREATE TABLE schedules_{user_id} (
                        module_name VARCHAR, 
                        discipline_name VARCHAR, 
                        direction_name VARCHAR, 
                        lesson_name VARCHAR, 
                        lesson_type VARCHAR, 
                        weekday VARCHAR,
                        lesson_time VARCHAR, 
                        teacher VARCHAR, 
                        team VARCHAR
                    );
                """)
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

    def save_schadules_data_to_db(self, *data, user_id=None):
        module_name, discipline_name, direction_name, lesson_name, lesson_type, weekday, lesson_time, teacher, team = data
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()
                cursor.execute(f"""
                            INSERT INTO schedules_{user_id} (module_name, discipline_name, direction_name, lesson_name, lesson_type, weekday, lesson_time, teacher, team) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """, (module_name, discipline_name, direction_name, lesson_name, lesson_type, weekday, lesson_time, teacher, team)
                               )
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

    def get_schedule_url(self):
        return self.find_element(ModeusLocators.SCHEDULE_URL, time=self.time)  # .get_attribute("href")

    def go_to(self, url):
        return self.get_connect(url)

    #
    def get_popover(self):
        return self.find_element(ModeusLocators.POPOVER, time=self.time)

    def get_teachers_name(self):
        return self.find_element(ModeusLocators.TEACHERS_NAME, time=self.time).text

    def get_h3_point(self):
        return self.find_element(ModeusLocators.H3_MY_SCHEDULE, time=self.time)
    #


class TeachersParsing(BaseClass):
    def create_teachers_table(self):
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    CREATE TABLE teachers_data (
                        id SERIAL PRIMARY KEY,
                        teacher_name VARCHAR,
                        teacher_phone VARCHAR,
                        teacher_email VARCHAR
                    )
                """)
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

    def get_pages(self):
        pages = self.find_elements(TeachersParsingLocators.PAGES_HREFS, time=self.time)
        urls = []
        for page in pages:
            urls.append(page.get_attribute("href"))
        return urls

    def go_to_teachers_page(self):
        url = 'https://urfu.ru/ru/about/personal-pages'
        return self.get_connect(url)

    def get_teachers_cards(self):
        try:
            return self.find_elements(TeachersParsingLocators.TEACHERS_CARDS, time=self.time)
        except TE:
            return []

    def save_teacher_data(self, *data):
        teacher_name, teacher_phone, teacher_email = data
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    INSERT INTO teachers_data (teacher_name, teacher_phone, teacher_email) VALUES (%s, %s, %s)
                    """, (teacher_name, teacher_phone, teacher_email)
                               )
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")
