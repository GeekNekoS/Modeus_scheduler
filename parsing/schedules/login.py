import time

import psycopg2
from selenium.webdriver.chrome.options import Options
from parsing.page_object import ModeusPage
from parsing.page_object import LoginPage
from selenium import webdriver
import os

from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')


def is_user_logedin_modeus(user_id):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * FROM users_modeus
                WHERE id = %s;
            """, (user_id,))
            users_data = cursor.fetchall()[0]

            chrome_options = Options()
            chrome_options.add_argument("--headless=new")
            driver = webdriver.Chrome()  # options=chrome_options
            driver.maximize_window()

            # login
            login_page = LoginPage(driver)
            login_page.go_to_modules_page()
            login_page.enter_login(users_data[1])
            login_page.enter_password(users_data[2])
            login_page.click_on_the_login_button()

            loged_in = login_page.check_logedin()
            if loged_in:
                return True
            else:
                return False

    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def login(page):
    page.go_to_modules_page()
    page.enter_login(os.getenv('LOGIN'))
    page.enter_password(os.getenv('PASSWORD'))
    page.click_on_the_login_button()

    return page
