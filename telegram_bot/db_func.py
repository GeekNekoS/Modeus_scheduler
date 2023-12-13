import psycopg2
import os

from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL_LOCAL')


def if_table_schedule_exists(user_id):
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

    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM schedules_{user_id}"
            cursor.execute(query)
            if not cursor.fetchall():
                return True
            else:
                return False
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def create_text_reviews_db():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE reviews (id INTEGER, teacher TEXT, opinions TEXT DEFAULT '');""")
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def text_review_creator(user_id, teacher, opinion):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO reviews (id, teacher, opinions) VALUES (%s, %s, %s);""",
                           (user_id, teacher, opinion)
                           )
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def get_text_reviews_this_teacher(teacher_name):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT opinions FROM reviews WHERE teacher = %s;""",
                           (teacher_name,)
                           )
            return cursor.fetchall()
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def leave_modeus_account(user_id):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""DROP TABLE schedules_{user_id}""")
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def find_teacher(name):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()

            cursor.execute("""SELECT * FROM teachers_data WHERE LOWER(teacher_name) = %s;""",
                           (name,)
                           )
            if not cursor.fetchall():
                return False
            else:
                return True
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def check_with_text_review(name, user_id):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM reviews WHERE LOWER(teacher) = %s AND id = %s;""",
                           (name, user_id)
                           )
            if not cursor.fetchall():
                return True
            else:
                return False
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def delete_text_review(user_id, teacher_name):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM reviews WHERE LOWER(teacher) = %s AND id = %s;""",
                           (teacher_name, user_id)
                           )
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def create_rating_reviews_db():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE rating_reviews (
                    id INTEGER,
                    teacher TEXT,
                    question_1 INTEGER,
                    question_2 INTEGER,
                    question_3 INTEGER,
                    question_4 INTEGER,
                    question_5 INTEGER,
                    question_6 INTEGER,
                    question_7 INTEGER,
                    question_8 INTEGER,
                    question_9 INTEGER,
                    question_10 INTEGER
                );
            """)
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def check_with_rating_review(name, user_id):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM rating_reviews WHERE LOWER(teacher) = %s AND id = %s;""",
                           (name, user_id)
                           )
            if not cursor.fetchall():
                return True
            else:
                return False
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def add_user_to_rating_db(user_id, teacher):
    try:
        with psycopg2.connect(DATABASE_URL) as postgres:
            cursor = postgres.cursor()
            cursor.execute("""
            INSERT INTO rating_reviews (
            id,
            teacher,
            question_1,
            question_2,
            question_3,
            question_4,
            question_5,
            question_6,
            question_7,
            question_8,
            question_9,
            question_10
            )
            VALUES (%s, %s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
            """, (user_id, teacher))
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def rating_review_creator(user_id, teacher, number_question, rating):
    try:
        with psycopg2.connect(DATABASE_URL) as connect:
            cursor = connect.cursor()
            cursor.execute(f"""UPDATE rating_reviews SET {number_question} = %s WHERE LOWER(teacher) = %s AND id = %s;""",
                           (rating, teacher, user_id)
                           )
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def delete_rating_review(user_id, teacher_name):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM rating_reviews WHERE LOWER(teacher) = %s AND id = %s; """,
                           (teacher_name, user_id)
                           )
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def get_rating_reviews_this_teacher(teacher):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM rating_reviews WHERE teacher = %s;""",
                           (teacher,)
                           )
            return cursor.fetchall()
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def get_all_rating_reviews():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT * FROM rating_reviews;"""
            )
            return cursor.fetchall()
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def rating_review_table_helper_creator():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE rating_reviews_helper (
                    teacher TEXT,
                    question_1 TEXT,
                    question_2 TEXT,
                    question_3 TEXT,
                    question_4 TEXT,
                    question_5 TEXT,
                    question_6 TEXT,
                    question_7 TEXT,
                    question_8 TEXT,
                    question_9 TEXT,
                    question_10 TEXT
                );
            """)
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def rating_review_table_helper_getter(teacher):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM rating_reviews_helper WHERE teacher = %s;""",
                           (teacher,))
            return cursor.fetchall()
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def rating_review_table_helper_dropper(teacher):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM rating_reviews_helper WHERE LOWER(teacher) = %s; """,
                           (teacher,)
                           )
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def rating_review_table_helper_dropper_all():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""DROP TABLE rating_reviews_helper; """)
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def rating_review_table_helper_setter(teacher, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    try:
        with psycopg2.connect(DATABASE_URL) as postgres:
            cursor = postgres.cursor()
            cursor.execute("""
            INSERT INTO rating_reviews_helper (
            teacher,
            question_1,
            question_2,
            question_3,
            question_4,
            question_5,
            question_6,
            question_7,
            question_8,
            question_9,
            question_10
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (teacher, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10))

    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")
        print('нет дело здесь')


def get_all_rating_reviews_helper():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT * FROM rating_reviews_helper;"""
            )
            return cursor.fetchall()
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def average_rating_reviews_creator():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE average_rating_reviews (
                    teacher TEXT,
                    question_1 FLOAT,
                    question_2 FLOAT,
                    question_3 FLOAT,
                    question_4 FLOAT,
                    question_5 FLOAT,
                    question_6 FLOAT,
                    question_7 FLOAT,
                    question_8 FLOAT,
                    question_9 FLOAT,
                    question_10 FLOAT
                );
            """)
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def average_rating_reviews_dropper():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""DROP TABLE average_rating_reviews""")
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def average_rating_reviews_setter(teacher, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    try:
        with psycopg2.connect(DATABASE_URL) as postgres:
            cursor = postgres.cursor()
            cursor.execute("""
            INSERT INTO average_rating_reviews (
            teacher,
            question_1,
            question_2,
            question_3,
            question_4,
            question_5,
            question_6,
            question_7,
            question_8,
            question_9,
            question_10
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (teacher, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10))
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")
