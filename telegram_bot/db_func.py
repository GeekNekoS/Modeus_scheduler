import sqlite3


def is_user(arg):
    with sqlite3.connect('tg_bot.sql') as sql:
        cur = sql.cursor()
        select = """
            SELECT * FROM users
            WHERE id = ?
        """
        cur.execute(select, (arg,))

        if not cur.fetchall():
            return False
        else:
            return True


def reg():
    sql = sqlite3.connect('tg_bot.sql')
    cur = sql.cursor()
    select = """
        CREATE TABLE IF NOT EXISTS users (
            id integer,
            activity integer,
            teacher_now text,
            modeus_logining integer
        )
    """
    cur.execute(select)
    sql.commit()
    cur.close()
    sql.close()


def add(arg):
    with sqlite3.connect('tg_bot.sql') as sql:
        cur = sql.cursor()
        select = """
        INSERT INTO users (id, activity, teacher_now, modeus_logining)
        VALUES (?, 0, 0, 0)
        """
        cur.execute(select, (arg,))
        sql.commit()


# def get():
#     with sqlite3.connect('tg_bot.sql') as sql:
#         cur = sql.cursor()
#         select = """
#         SELECT * FROM users
#         """
#         cur.execute(select)
#         return cur.fetchall()


def reg_reviews():
    sql = sqlite3.connect('tg_bot_reviews.sql')
    cur = sql.cursor()
    select = """
        CREATE TABLE IF NOT EXISTS reviews (
            teacher text, 
            opinions text
        )
    """
    cur.execute(select)
    sql.commit()
    cur.close()
    sql.close()


def teacher_now(teacher, id_user):
    with sqlite3.connect('tg_bot.sql') as sql:
        cur = sql.cursor()
        select = """
        UPDATE users
        SET teacher_now = ?
        WHERE id = ?
        """
        cur.execute(select, (teacher, id_user))
        sql.commit()


# def teacher_now2(id_user):
#     with sqlite3.connect('tg_bot.sql') as sql:
#         cur = sql.cursor()
#         select = """
#         UPDATE users
#         SET teacher_now = '0'
#         WHERE id = ?
#         """
#         cur.execute(select, (id_user,))
#         sql.commit()


# def get_teacher_status(arg):
#     with sqlite3.connect('tg_bot.sql') as sql:
#         cur = sql.cursor()
#         select = """
#         SELECT teacher_now FROM users
#         WHERE id = ?
#         """
#         cur.execute(select, (arg,))
#         return cur.fetchall()[0][0]


# def add_review(user_id, opinion):
#     with sqlite3.connect('tg_bot.sql') as sql:
#         cur = sql.cursor()
#         select = """
#                 SELECT teacher_now FROM users
#                 WHERE id = ?
#                 """
#         cur.execute(select, (user_id,))
#         a = cur.fetchall()[0][0]
#     with sqlite3.connect('tg_bot_reviews.sql') as sql:
#         cur = sql.cursor()
#         select = """
#         INSERT INTO reviews (teacher, opinions)
#         VALUES (?, ?)
#         """
#         cur.execute(select, (a, opinion))
#         sql.commit()


def review_creator(teacher, opinion):
    with sqlite3.connect('tg_bot_reviews.sql') as sql:
        cur = sql.cursor()
        select = """
        INSERT INTO reviews (teacher, opinions)
        VALUES (?, ?)
        """
        cur.execute(select, (teacher, opinion))
        sql.commit()


# def add_review2(user_id, opinion):
#     with sqlite3.connect('tg_bot.sql') as sql:
#         cur = sql.cursor()
#         select = """
#                 SELECT teacher_now FROM users
#                 WHERE id = ?
#                 """
#         cur.execute(select, (user_id,))
#         teach = cur.fetchall()[0][0]
#     with sqlite3.connect('tg_bot_reviews.sql') as sql:
#         cur = sql.cursor()
#         select = """
#                 SELECT opinions FROM reviews
#                 WHERE teacher = ?
#                 """
#         cur.execute(select, (teach,))
#         a = cur.fetchall()[0][0]
#         print(a, 'a')
#         all_opinions = a + '\n'+'\n'+'\n'+opinion
#         print(all_opinions, 'all_opinions')
#     # with sqlite3.connect('tg_bot_reviews.sql') as sql:
#         select = """
#         UPDATE reviews
#         SET opinions = ?
#         WHERE teacher = ?
#         """
#         cur.execute(select, (all_opinions, teach))
#         sql.commit()


# def check_with_review(teacher):
#     with sqlite3.connect('tg_bot_reviews.sql') as sql:
#         cur = sql.cursor()
#         select = """
#             SELECT teacher FROM reviews
#             WHERE teacher = ?
#         """
#         cur.execute(select, (teacher,))
#
#         if not cur.fetchall():
#             return False
#         else:
#             return True


# def is_teacher(arg):
#     with open('teachers.txt', encoding='utf-8') as f:
#         teachers = f.read().lower().split('\n')
#         if arg.lower() in teachers:
#             return True
#         else:
#             return False


# def get_reviews():
#     with sqlite3.connect('tg_bot_reviews.sql') as sql:
#         cur = sql.cursor()
#         select = """
#                 SELECT * FROM reviews
#                 """
#         cur.execute(select)
#         return cur.fetchall()


def get_reviews_this_teacher(teacher_name):
    with sqlite3.connect('tg_bot_reviews.sql') as sql:
        cur = sql.cursor()
        select = """
                SELECT opinions FROM reviews
                WHERE teacher = ?
                """
        cur.execute(select, (teacher_name,))
        return cur.fetchall()


# def set_activity_status1(arg):
#     with sqlite3.connect('tg_bot.sql') as sql:
#         cur = sql.cursor()
#         select = """
#         UPDATE users
#         SET activity = 1
#         WHERE id = ?
#         """
#         cur.execute(select, (arg,))
#         sql.commit()


# def set_activity_status0(arg):
#     with sqlite3.connect('tg_bot.sql') as sql:
#         cur = sql.cursor()
#         select = """
#         UPDATE users
#         SET activity = 0
#         WHERE id = ?
#         """
#         cur.execute(select, (arg,))
#         sql.commit()


# def get_activity_status(arg):
#     with sqlite3.connect('tg_bot.sql') as sql:
#         cur = sql.cursor()
#         select = """
#         SELECT activity FROM users
#         WHERE id = ?
#         """
#         cur.execute(select, (arg,))
#         return cur.fetchall()[0][0]
