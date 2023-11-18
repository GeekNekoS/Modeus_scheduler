from parsing.locators import *
from parsing.base_page import BaseClass
import psycopg2


class LoginPage(BaseClass):
    # Log in
    def enter_login(self, login):
        return self.find_element(LoginLocators.LOGIN_INPUT, time=self.time).send_keys(login)

    def enter_password(self, password):
        return self.find_element(LoginLocators.PASSWORD_INPUT, time=self.time).send_keys(password)

    def click_on_the_login_button(self):
        return self.find_element(LoginLocators.LOGIN_BUTTON, time=self.time).click()

    # Log out


class ModeusPage(BaseClass):
    def create_lessons_table(self):
        try:
            with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    CREATE TABLE lessons (
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

    def save_lesson_data_to_db(self, *data):
        lesson_name, module_url = data
        try:
            with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    INSERT INTO lessons (lesson, module_url) VALUES (%s, %s)
                    """, (lesson_name, module_url)
                               )
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

    def create_directions_table(self):
        try:
            with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    CREATE TABLE directions (
                        id SERIAL PRIMARY KEY,
                        direction VARCHAR,
                        schedule_url VARCHAR,
                        foreign_key INT
                    );
                """)
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

    def get_lessons_data(self):
        lessons_info = None
        try:
            with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
                cursor = connection.cursor()
                query = """SELECT * FROM lessons"""
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

    def save_directions_data_to_db(self, *data):
        direction_name, direction_url, lesson_id = data
        try:
            with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    INSERT INTO directions (direction, schedule_url, foreign_key) VALUES (%s, %s, %s)
                    """, (direction_name, direction_url, lesson_id)
                               )
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")
