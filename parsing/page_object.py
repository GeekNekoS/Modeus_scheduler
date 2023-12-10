import time

from parsing.locators import *
from parsing.base_page import BaseClass
from selenium.common.exceptions import TimeoutException as TE


class LoginPage(BaseClass):
    # Log in
    def enter_login(self, login):
        return self.find_element(LoginLocators.LOGIN_INPUT, time=self.time).send_keys(login)

    def enter_password(self, password):
        return self.find_element(LoginLocators.PASSWORD_INPUT, time=self.time).send_keys(password)

    def click_on_the_login_button(self):
        return self.find_element(LoginLocators.LOGIN_BUTTON, time=self.time).click()

    def check_logedin(self):
        try:
            self.find_element(LoginLocators.H4_CHOOSING_MODULES, time=self.time)
            return True
        except:
            return False

    # Log out


class ModeusPage(BaseClass):
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

    def get_schedule_url(self):
        return self.find_element(ModeusLocators.SCHEDULE_URL, time=self.time)  # .get_attribute("href")

    def go_to(self, url):
        return self.get_connect(url)

    #
    def get_popover(self):
        return self.find_element(ModeusLocators.POPOVER, time=self.time)

    def get_teachers_name(self):
        return self.find_element(ModeusLocators.TEACHERS_NAME, time=self.time).text.replace("\n", ", ")

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
