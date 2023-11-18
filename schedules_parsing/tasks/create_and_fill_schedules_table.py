from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from schedules_parsing.page_object import LoginPage
from schedules_parsing.page_object import ModeusPage
from selenium import webdriver
import pyautogui
import os

from dotenv import load_dotenv
load_dotenv()


def create_and_fill_schedules_table():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    # login
    login_page.go_to_modules_page()
    login_page.enter_login(os.getenv('LOGIN'))
    login_page.enter_password(os.getenv('PASSWORD'))
    login_page.click_on_the_login_button()

    # Create and fill lessons table
    modeus_page = ModeusPage(driver)
