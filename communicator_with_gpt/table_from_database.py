import psycopg2

def create_table_file():
    # подключение к базе данных локально
    url = 'postgresql://postgres:1@localhost:5432/schedules'
    conn = psycopg2.connect(url)

    # получение 100 строк данных из базы
    curs =  conn.cursor()
    curs.execute('SELECT * FROM public.schedules')
    users_lessons = curs.fetchmany(size=100)
    curs.close()
    conn.close()

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
