import logging
import telebot
from telebot import types
import random_topics0
import markups
import db_func
import sqlite3

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "6417309065:AAFotgeFNidq8gg-T7fDxLfI3j91wXKM2FM"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'Приветствую тебя в нашем боте!\nНиже тебе доступны команды',
                     reply_markup=markups.start_markup())


@bot.message_handler(content_types=['text'])
def text_input(message):
    if message.text.lower() == 'старт':
        bot.send_message(message.chat.id, db_func.reg())
        main(message)
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, чё как?')
    elif message.text.lower() == 'помощь':
        bot.send_message(message.chat.id, 'Бог в помощь')
    elif message.text.lower() == 'техника безопасности':
        # check_auth_with_message(message, safety)
        safety(message)
    elif message.text.lower() == 'смотреть правила':
        if random_topics0.progress() == '94%':
            rules(message)
            bot.send_message(message.chat.id, f'Поздравляю!\nВы ознакомились со всеми правилами')
        elif random_topics0.progress() == '100%':
            bot.send_message(message.chat.id, 'Вы уже ознакомились со всеми правилами! :)')
        else:
            rules(message)
    elif message.text.lower() == 'назад в меню':
        start(message)
    elif message.text.lower() == 'мой прогресс':
        bot.send_message(message.chat.id, random_topics0.progress())
    elif message.text.lower() == 'пользователи':
        all_users(message)
    # else:
       # bot.send_message(message.from_user.id, 'Не понимаю о чём вы')


# def check_auth_with_message(message, cb):

# bot.send_message(message.chat.id, random_topics.pr())


@bot.callback_query_handler(func=lambda call: True)
def main(message):
    bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    name = message.text
    sql = sqlite3.connect('tg_bot.sql')
    cur = sql.cursor()

    cur.execute(f"INSERT INTO users (name) VALUES ('%s')" % name)
    sql.commit()
    cur.close()
    sql.close()

    bot.send_message(message.chat.id, 'Записал!')


def all_users(message):
    sql = sqlite3.connect('tg_bot.sql')
    cur = sql.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'{el[1]}\n'

    cur.close()
    sql.close()

    bot.send_message(message.chat.id, info)


def safety(message):
    # random_topics.create_statistics_file()
    # random_topics.tell_topic()
    text_msg = (f'В этом разделе вы можете:\n'
                f''
                f'---ознакомиться с правилами техники безопасности на занятиях физкультуры\n'
                f''
                f'---отслеживать свой прогресс в изучении техники безопасности')
    bot.send_message(message.chat.id, text_msg,
                     reply_markup=markups.safety_markup())


def rules(message):
    msg = random_topics0.tell_topic()
    bot.send_message(message.chat.id, msg)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
  #  bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
