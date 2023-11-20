import psycopg2


def create_modeus_db():
    try:
        with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE users_modeus (
                    id integer,
                    login VARCHAR,
                    password VARCHAR
                );
            """)
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def reg_user_in_modeus(user_id, user_login, user_password):
    try:
        with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
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


def is_user_login_modeus(user_id):
    try:
        with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
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


def create_text_reviews_db():
    try:
        with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE reviews (
                    teacher TEXT, 
                    opinions TEXT DEFAULT ''
                );
            """)
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def review_creator(teacher, opinion):
    try:
        with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
            cursor = connection.cursor()
            cursor.execute("""
            INSERT INTO reviews (
            teacher,
            opinions
            )
            VALUES (%s, %s);
            """, (teacher, opinion))
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def get_reviews_this_teacher(teacher_name):
    try:
        with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT opinions FROM reviews
                WHERE teacher = %s;
            """, (teacher_name,))
            return cursor.fetchall()
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")
