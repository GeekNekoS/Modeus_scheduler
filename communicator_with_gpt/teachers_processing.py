import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_reviews_table() -> list:
    db_url = os.getenv("DATABASE_URL")
    try:
        with psycopg2.connect(db_url) as connection:
            table = []
            cursor = connection.cursor()
            query = "SELECT * FROM average_rating_reviews"
            cursor.execute(query)
            for lesson_data in cursor.fetchall():
                table.append(lesson_data)
            return table
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def get_avg_teacher_grades():
    teachers_table = get_reviews_table()
    teachers_avg_grades = ""
    for teacher_data in teachers_table:
        sum_of_grades = sum(teacher_data[1:])
        count_of_grades = len([x for x in teacher_data[1:] if x > 0])
        avg_teacher_grade = sum_of_grades // count_of_grades
        teachers_avg_grades += f"{teacher_data[0].title()} - {avg_teacher_grade}\n"
    return teachers_avg_grades

