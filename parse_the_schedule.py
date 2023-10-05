# Тут много говнокода! Я исправлю, честно, только позже - Neko

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()

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


def reg():
    url = 'https://urfu.modeus.org/'
    driver.maximize_window()

    try:
        get_connect(url)
        time.sleep(2)

        user_name_input = driver.find_element(By.XPATH, "//input[@placeholder='proverka@example.com']")
        user_name_input.send_keys(os.getenv('LOGIN'))
        time.sleep(1)

        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
        password_input.send_keys(os.getenv('PASSWORD'))
        time.sleep(1)

        login_button = driver.find_element(By.XPATH, "//span[@class='submit']")
        login_button.click()
        time.sleep(2)

        return driver

    except Exception as exception:
        print(f"\033[38;5;{196}mWasted ψ(▼へ▼メ)\033[0;0m" + f"\n{exception}")
        return None


def parse_math_basic_level():
    get_connect('https://urfu.modeus.org/learning-path-selection/menus/45f2857b-6745-4d7a-8677-002f0b3e02e0')
    time.sleep(5)

    math_button = driver.find_element(By.XPATH, "//div[text()=' Математика ']")
    math_button.click()
    time.sleep(1)

    basic_level_button = driver.find_element(By.XPATH, "//div[text()=' Математика. Базовый уровень. ']")
    basic_level_button.click()
    time.sleep(1)

    module_schedule_button = driver.find_element(By.XPATH, "//a[text()=' Расписание модуля ']")
    module_schedule_button.click()
    time.sleep(1)

    # Поздравляю, вы на странице, которую нужно спарсить
    time.sleep(60*10)


def parse_itis_4():
    get_connect('https://urfu.modeus.org/learning-path-selection/menus/45f2857b-6745-4d7a-8677-002f0b3e02e0')
    time.sleep(5)

    itis_button = driver.find_element(By.XPATH, "//div[text()=' Информационные технологии и сервисы ']")
    itis_button.click()
    time.sleep(1)

    time.sleep(60 * 10)


def main():
    reg()
    parse_math_basic_level()
    # parse_itis_4()


if __name__ == "__main__":
    main()
