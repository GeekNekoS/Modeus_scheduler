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

    modules_page.create_schedules_table()

    parsed_data = []

    discipline_names = []  # remove_this
    direction_names = []
    disciplines_page_urls = []

    # Modules parsing
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

        # Disciplines parsing
        disciplines_page_url = driver.current_url
        disciplines_page_urls.append(disciplines_page_url)
        disciplines = modeus_page.get_disciplines()
        for i in range(len(disciplines)):
            disciplines = modeus_page.get_disciplines()
            discipline_name = disciplines[i].text  # <==
            discipline_names.append(discipline_name)
            discipline_xpath = f"//div[@class='item-name' and text()=' {discipline_name} ']"

            discipline_link = modeus_page.find_element_by_xpath(discipline_xpath)

            ActionChains(driver).key_down(Keys.CONTROL).click(discipline_link).key_up(Keys.CONTROL).perform()
            pyautogui.hotkey('ctrl', 't')

            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            driver.close()

            window_after = driver.window_handles[0]
            driver.switch_to.window(window_after)

            # Directions parsing
            directions = modeus_page.get_directions()
            for i in range(len(directions)):
                directions = modeus_page.get_directions()
                direction_name = directions[i].text  # <==
                direction_names.append(direction_name)

            direction_buttons_xpath = ".//div[@class='item-name']/parent::div/parent::td/parent::tr[@class='item-row ng-star-inserted']"
            direction_buttons = modeus_page.find_elements_by_xpath(direction_buttons_xpath)

            # Schedules parsing
            for direction_button in direction_buttons:
                direction_name = direction_button.text
                print(direction_name)
                modules_page.save_schadules_data_to_db(module_name, discipline_name, direction_name)

            modeus_page.go_to_disciplines_page(disciplines_page_url)

            print()
            print()
            print()
            print()
            print()

        modeus_page.go_to_modules_page()

    # -=-= Test saving =-=-
    # for direction_data in parsed_data:
    #     print(f"{direction_data[0]}; {direction_data[1]}")
    # -=-=-=-=-=-=-=-=-=-=-

    driver.close()
    return driver


create_and_fill_schedules_table()
