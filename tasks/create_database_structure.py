import os
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

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

    # Modules
    modules = driver.find_elements(By.XPATH, "//tbody/tr//span")

    lessons = []
    for i in range(len(modules)):
        modules = driver.find_elements(By.XPATH, "//tbody/tr//span")

        link = modules[i]

        ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        pyautogui.hotkey('ctrl', 't')

        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.close()

        window_after = driver.window_handles[0]
        driver.switch_to.window(window_after)

        cur_url = driver.current_url
        print(cur_url)

        parsed_lessons = driver.find_elements(By.XPATH, "//div[@class='item-name']")
        for lesson in parsed_lessons:
            lessons.append(lesson.text)

        get_connect(url)
        time.sleep(3)

    print(lessons)

    return driver


def main():
    parse()


if __name__ == "__main__":
    main()


# print(driver.window_handles)
# print(driver.current_url)

# driver.execute_script("window.open('https://urfu.modeus.org/learning-path-selection/menus/45f2857b-6745-4d7a-8677-002f0b3e02e0', 'new window')")
# window_after = driver.window_handles[1]
# driver.switch_to.window(window_after)
