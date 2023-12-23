from work_with_db.teachers_table import *
from parsing.page_object import TeachersParsing
from selenium import webdriver


def parse_teachers_data():
    driver = webdriver.Chrome()

    # Working with personal pages
    teachers_pages = TeachersParsing(driver)

    create_teachers_table()
    teachers_pages.go_to_teachers_page()

    urls = teachers_pages.get_pages()
    for url in urls:
        teachers_page.get_connect(url)
        teachers_cards = teachers_pages.get_teachers_cards()
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

            save_teacher_data(teacher_name, teacher_phone, teacher_email)

            print(teacher_name, teacher_phone, teacher_email, "\n")


parse_teachers_data()
