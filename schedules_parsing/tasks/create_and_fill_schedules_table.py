from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from schedules_parsing.page_object import LoginPage
from schedules_parsing.page_object import ModeusPage
from selenium import webdriver
import pyautogui
from schedules_parsing.tasks.login import login
import time

from dotenv import load_dotenv
load_dotenv()


def create_and_fill_schedules_table():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    # login
    login(login_page)

    # Create and fill lessons table
    modeus_page = ModeusPage(driver)

    modeus_page.go_to_modules_page()
    time.sleep(1)
