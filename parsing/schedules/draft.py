from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from parsing.page_object import LoginPage
from parsing.page_object import ModulesPages

from parsing.page_object import ModeusPage

from selenium import webdriver
import pyautogui
from parsing.schedules.login import login
from selenium.webdriver.chrome.options import Options
import time
import os

from dotenv import load_dotenv
load_dotenv()


# DATABASE_URL = os.getenv('DATABASE_URL')


def create_and_fill_schedules_table():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome()  # options=chrome_options
    # driver.maximize_window()

    # login
    login_page = LoginPage(driver)
    login_page.go_to_modules_page()
    login_page.enter_login(os.getenv('LOGIN'))
    login_page.enter_password(os.getenv('PASSWORD'))
    login_page.click_on_the_login_button()

    # Create and fill lessons table
    modules_page = ModulesPages(driver)
    modules_page.go_to_modules_page()

    modeus_page = ModulesPages(driver)

    parsed_data = []

    modules_links = []
    modules = modeus_page.get_modules()
    for i in range(len(modules)):
        modules = modeus_page.get_modules()
        module_name = modules[i].text  # <==
        module_link = modules[i]
        ActionChains(driver).key_down(Keys.CONTROL).click(module_link).key_up(Keys.CONTROL).perform()
        pyautogui.hotkey('ctrl', 't')

        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.close()

        window_after = driver.window_handles[0]
        driver.switch_to.window(window_after)

        module_url = driver.current_url
        modules_links.append(module_url)

        disciplines_page_url = driver.current_url
        disciplines = modeus_page.get_disciplines()
        for i in range(len(disciplines)):
            disciplines = modeus_page.get_disciplines()
            discipline_name = disciplines[i].text  # <==
            discipline_xpath = f"//div[@class='item-name' and text()=' {discipline_name} ']"

            discipline_link = modeus_page.find_element_by_xpath(discipline_xpath)

            ActionChains(driver).key_down(Keys.CONTROL).click(discipline_link).key_up(Keys.CONTROL).perform()
            pyautogui.hotkey('ctrl', 't')

            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            driver.close()

            window_after = driver.window_handles[0]
            driver.switch_to.window(window_after)

            module_url = driver.current_url
            modules_links.append(module_url)

            # Начало парсинга направлений
            direction_name = None

            directions = modeus_page.get_directions()

            for i in range(len(directions)):
                directions = modeus_page.get_directions()
                direction_name = directions[i].text  # <==

                if discipline_name != direction_name:
                    print("Название направления: " + direction_name)
                print()

                # print("Название направления: " + direction_name)
            #

            # print(f"Go to: {disciplines_page_url}")
            modeus_page.go_to_disciplines_page(disciplines_page_url)

        modeus_page.go_to_modules_page()

    # -=-= Test saving =-=-
    # for direction_data in parsed_data:
    #     print(f"{direction_data[0]}; {direction_data[1]}")
    # -=-=-=-=-=-=-=-=-=-=-

    driver.close()
    return driver


create_and_fill_schedules_table()
