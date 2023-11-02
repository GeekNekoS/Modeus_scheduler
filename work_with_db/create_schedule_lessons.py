import os
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

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
        print(direction)

        get_connect(direction[2])
        time.sleep(5)

    return driver


def main():
    parse()


if __name__ == "__main__":
    main()
