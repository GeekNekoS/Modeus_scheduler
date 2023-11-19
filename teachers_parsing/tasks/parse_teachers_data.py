from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from schedules_parsing.page_object import LoginPage
from schedules_parsing.page_object import TeachersParsing
from selenium import webdriver
import pyautogui
import os

import time

from dotenv import load_dotenv
load_dotenv()


def parse_teachers_data():
    driver = webdriver.Chrome()

    # Working with modeus personal pages
    modeus_page = TeachersParsing(driver)

    modeus_page.create_teachers_table()

    modeus_page.go_to_somewhere()
    teachers_cards = modeus_page.get_teachers_cards()
    for teacher_data in teachers_cards:
        teacher_name = modeus_page.get_name()
        print(teacher_name.text)
    time.sleep(1)


parse_teachers_data()