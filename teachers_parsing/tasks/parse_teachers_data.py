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

    pages = modeus_page.get_pages()
    for page in pages:
        print(page)

    modeus_page.create_teachers_table()
    modeus_page.go_to_somewhere()
    teachers_cards = modeus_page.get_teachers_cards()
    for teacher_card in teachers_cards:
        teacher_data = teacher_card.text.split("\n")
        teacher_name = teacher_data[0]
        teacher_phone = "Нет данных"
        teacher_email = "Нет данных"
        for item in teacher_data:
            if "Телефон: " in item:
                teacher_phone = item.replace("Телефон: ", "")
            if "Электронная почта: " in item:
                teacher_email = item.replace("Электронная почта: ", "")

        print(teacher_name, teacher_phone, teacher_email, "\n")

    time.sleep(1)


parse_teachers_data()