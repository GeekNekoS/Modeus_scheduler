import psycopg2


url = 'postgresql://postgres:1@localhost:5432/schedules'


def create_modeus_db():
    try:
        with psycopg2.connect(url) as connection:
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


def reg_user_in_modeus(user_id, user_login, user_password):
    try:
        with psycopg2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            INSERT INTO users_modeus (
            id,
            login,
            password
            )
            VALUES (%s, %s, %s);
            """, (user_id, user_login, user_password))
    except error:
        pass
        # print(f"Can`t establish connection to database: {ex}\n")


def is_user_login_modeus(user_id):
    try:
        with psycopg2.connect(url) as connection:
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
        with psycopg2.connect(url) as connection:
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
        with psycopg2.connect(url) as connection:
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
        with psycopg2.connect(url) as connection:
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
        with psycopg2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM users_modeus
                WHERE id = %s;
            """, (user_id,))
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def get_all():
    try:
        with psycopg2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * FROM users_modeus;
            """)
            return cursor.fetchall()
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def update_user_modeus_preference(preference, user_id):
    try:
        with psycopg2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE users_modeus
                SET preference = %s
                WHERE id = %s;
            """, (preference, user_id))
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")
