import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def table_from_db(user_id) -> list:
    db_url = os.getenv("DATABASE_URL")
    try:
        with psycopg2.connect(db_url) as connection:
            table = []
            cursor = connection.cursor()
            query = f"SELECT * FROM schedules_{user_id}"
            cursor.execute(query)
            for lesson_data in cursor.fetchall():
                if "Информационные технологии и сервисы" in lesson_data[-1]:
                    table.append(make_itis_data_shorter(lesson_data))
                elif "История России" in lesson_data[-1]:
                    table.append(make_history_data_shorter(lesson_data))
                elif "Иностранный язык (английский)" in lesson_data[-1]:
                    table.append(make_english_data_shorter(lesson_data))
                else:
                    table.append(lesson_data)
        return table
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def make_itis_data_shorter(lesson_data) -> list:
    short_team = lesson_data[-1].replace("Информационные технологии и сервисы", "ИТИС")
    short_data = lesson_data[:-1] + (short_team,)
    return short_data


def make_history_data_shorter(lesson_data) -> list:
    short_team = lesson_data[-1].replace("История России", "История")
    short_data = lesson_data[:-1] + (short_team,)
    return short_data


def make_english_data_shorter(lesson_data) -> list:
    short_team = lesson_data[-1].replace("Иностранный язык (английский)", "Английский язык")
    short_data = lesson_data[:-1] + (short_team,)
    return short_data


def get_uniq_teams(table) -> list:
    teams = set()
    for lesson_data in table:
        teams.add(lesson_data[-1])
    teams = sorted(teams)
    return teams


def link_teams_and_lessons(table, teams) -> dict:
    lessons_for_teams = dict.fromkeys(teams, "")
    for lesson_data in table:
        lessons_for_teams[lesson_data[-1]] += f"({lesson_data[2]},{lesson_data[3]},{lesson_data[4]})/"
    return lessons_for_teams

def get_user_lessons_table(user_id):
    db_table = table_from_db(user_id)
    uniq_teams = get_uniq_teams(db_table)
    teams_and_lessons = link_teams_and_lessons(db_table, uniq_teams)

    with open(f"temp_files\\schedule_{user_id}.txt", "w", encoding="utf-8") as f:
        for team, data in teams_and_lessons.items():
            f.write(f"{team}/{data[:-1]}.\n")
