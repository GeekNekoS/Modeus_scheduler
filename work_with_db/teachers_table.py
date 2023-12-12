import os
import psycopg2

from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')  # DATABASE_URL


def create_teachers_table():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE teachers_data (
                    id SERIAL PRIMARY KEY,
                    teacher_name VARCHAR,
                    teacher_phone VARCHAR,
                    teacher_email VARCHAR
                )
            """)
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def save_teacher_data(*data):
    teacher_name, teacher_phone, teacher_email = data
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO teachers_data (teacher_name, teacher_phone, teacher_email) VALUES (%s, %s, %s)
                """, (teacher_name, teacher_phone, teacher_email)
                           )
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")
