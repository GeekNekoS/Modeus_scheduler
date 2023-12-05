import psycopg2
import os

from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')


def if_table_schedule_exists(user_id):
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


def create_modeus_db():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE users_modeus (
                    id INTEGER,
                    login VARCHAR,
                    password VARCHAR,
                    preference TEXT
                );
            """)
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def is_user_login_modeus(user_id):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * FROM users_modeus
                WHERE id = %s;
            """, (user_id,))
            if not cursor.fetchall():
                return False
            else:
                return True
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def reg_user_in_modeus(user_id, user_login, user_password):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            INSERT INTO users_modeus (
            id,
            login,
            password
            )
            VALUES (%s, %s, %s);
            """, (user_id, user_login, user_password))
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def create_text_reviews_db():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE reviews (
                    id INTEGER,
                    teacher TEXT, 
                    opinions TEXT DEFAULT ''
                );
            """)
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def text_review_creator(user_id, teacher, opinion):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            INSERT INTO reviews (
            id,
            teacher,
            opinions
            )
            VALUES (%s, %s, %s);
            """, (user_id, teacher, opinion))
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def get_text_reviews_this_teacher(teacher_name):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT opinions FROM reviews
                WHERE teacher = %s;
            """, (teacher_name,))
            return cursor.fetchall()
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def leave_modeus_account(user_id):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM users_modeus
                WHERE id = %s;
            """, (user_id,))
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def update_user_modeus_preference(preference, user_id):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE users_modeus
                SET preference = %s
                WHERE id = %s;
            """, (preference, user_id))
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def find_teacher(name):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:  # <== url2
            cursor = connection.cursor()

            cursor.execute("""
                SELECT * FROM teachers_data
                WHERE LOWER(teacher_name) = %s;
            """, (name,))
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
            cursor.execute("""
                SELECT * FROM reviews
                WHERE LOWER(teacher) = %s
                AND id = %s;
            """, (name, user_id))
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
            cursor.execute("""
                DELETE FROM reviews
                WHERE LOWER(teacher) = %s
                AND id = %s;
            """, (teacher_name, user_id))
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
            cursor.execute("""
                SELECT * FROM rating_reviews
                WHERE LOWER(teacher) = %s
                AND id = %s;
            """, (name, user_id))
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
            cursor.execute(f"""
                UPDATE rating_reviews
                SET {number_question} = %s
                WHERE LOWER(teacher) = %s
                AND id = %s;
            """, (rating, teacher, user_id))
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def delete_rating_review(user_id, teacher_name):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM rating_reviews
                WHERE LOWER(teacher) = %s
                AND id = %s;
            """, (teacher_name, user_id))
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def get_rating_reviews_this_teacher(teacher):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * FROM rating_reviews
                WHERE teacher = %s;
            """, (teacher,))
            return cursor.fetchall()
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")
