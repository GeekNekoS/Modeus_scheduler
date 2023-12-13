import os
import psycopg2

from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')  # DATABASE_URL


def create_schedules_table(user_id=None):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
                CREATE TABLE schedules_{user_id} (
                    direction_name VARCHAR, 
                    lesson_type VARCHAR, 
                    weekday VARCHAR,
                    lesson_time VARCHAR, 
                    teacher VARCHAR, 
                    team VARCHAR
                );
            """)
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def save_schedules_data_to_db(data, user_id=None):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            for row in data:
                direction_name, lesson_type, weekday, lesson_time, teacher, team = row
                cursor.execute(f"""
                            INSERT INTO schedules_{user_id} (direction_name, lesson_type, weekday, lesson_time, teacher, team)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """, (direction_name, lesson_type, weekday, lesson_time, teacher, team)
                               )
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")
