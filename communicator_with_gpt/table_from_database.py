import psycopg2
import  os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("database_url")

def create_table_file(user_id):

    # подключение к базе данных локально
    users_lessons = None
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM schedules_{user_id}"
            cursor.execute(query)
            users_lessons = cursor.fetchall()
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")

    # создание словаря с ключами в виде названия команд
    teams = {}
    for lesson in users_lessons:
        teams[f"{lesson[-1]}/{lesson[1]}/"] = ""

    # добавление к каждой команде соответствующие занятия
    for lesson in users_lessons:
        teams[f"{lesson[-1]}/{lesson[1]}/"]+=f"({lesson[3]},{lesson[4]})/"

    # создание текстовой таблицы для отправки
    with open("output_table.txt", "w", encoding="utf-8") as table:
        for i in teams:
            table.write(f"{i}{teams[i][:-1]}.\n")
