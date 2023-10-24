import os
import random
import string
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

from dotenv import load_dotenv
load_dotenv()


def create_new_email():
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

    # Modules
    modules = driver.find_elements(By.XPATH, "//tbody/tr//span")

    # Работает!!! Осталось только найти способ автоматически получать эту ссылку
    # driver.execute_script("window.open('https://urfu.modeus.org/learning-path-selection/menus/45f2857b-6745-4d7a-8677-002f0b3e02e0', 'new window')")
    # window_after = driver.window_handles[1]
    # driver.switch_to.window(window_after)

    print(driver.current_url)

    time.sleep(1)

    # link = driver.find_element(By.LINK_TEXT, "Выбор модулей")
    # link.click()
    # print(link)

    link = modules[0]

    # Работает!!! но не открывает в новой вкладке
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    # # ActionChains(driver).key_down(Keys.COMMAND).send_keys(Keys.COMMAND + 't').click(link).perform()  # Keys.CONTROL
    #
    # window_after = driver.window_handles[1]
    # driver.switch_to.window(window_after)

    # link.send_keys(Keys.COMMAND + 't')
    import pyautogui
    pyautogui.hotkey('ctrl', 't')
    print('OK')

    cur_url = driver.current_url
    print(driver.current_url)

    # time.sleep(10)

    lessons = driver.find_elements(By.XPATH, "//div[@class='item-name']")
    print([i.text for i in lessons])

    return driver


def main():
    create_new_email()


if __name__ == "__main__":
    main()
