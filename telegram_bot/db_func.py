import psycopg2
import os

from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')


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


def review_creator(user_id, teacher, opinion):
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


def get_reviews_this_teacher(teacher_name):
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