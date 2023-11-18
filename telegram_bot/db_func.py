import sqlite3


def reg():
    sql = sqlite3.connect('tg_bot.sql')
    cur = sql.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto increment primary key, name, status)")
    sql.commit()
    cur.close()
    sql.close()

    return 'Введите ваше имя:'


# def user_name(message):





'''def add_user(id, name):
  with sql.connect('db.sqlite') as db:
    curs = db.cursor()

    query_select = "SELECT user_id FROM users WHERE user_id = ?"
    curs.execute(query_select, (id,))

    if curs.fetchall():
      return 'Уже зарегистрирован'

    query_select = "SELECT user_name FROM users WHERE user_name = ?"
    curs.execute(query_select, (name,))

    if curs.fetchall():
      return 'Имя занято'

    query_insert = """
      INSERT INTO users (user_id, user_name, date_create)
      VALUES (?, ?, ?)
    """
    curs.execute(query_insert,(id, name, dt_now))
    db.commit()'''