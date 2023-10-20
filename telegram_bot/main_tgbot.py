import logging
import telebot
from telebot import types
import random_topics0
import markups

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
        bot.send_message(message.chat.id, """
    Доступные команды:
    /hello
    # /learn_the_safety_rules_in_the_gym
    # /leave_a_review_about_the_teacher
    """)
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, чё как?')
    elif message.text.lower() == 'помощь':
        bot.send_message(message.chat.id, 'Бог в помощь')
    elif message.text.lower() == 'техника безопасности':
        # check_auth_with_message(message, safety)
        safety(message)
    elif message.text.lower() == 'смотреть правила':
        rules(message)
    elif message.text.lower() == 'назад в меню':
        start(message)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю о чём вы')


# def check_auth_with_message(message, cb):

# bot.send_message(message.chat.id, random_topics.pr())


@bot.callback_query_handler(func=lambda call: True)
def safety(message):
    # random_topics.create_statistics_file()
    # random_topics.tell_topic()
    text_msg = (f'В этом разделе вы можете:\n'
                f'---ознакомиться с правилами техники безопасности на занятиях физкультуры\n'
                f'---отслеживать свой прогресс в изучении техники безопасности')
    bot.send_message(message.chat.id, text_msg,
                     reply_markup=markups.safety_markup())


def rules(message):
    msg = random_topics0.tell_topic()
    bot.send_message(message.chat.id, msg)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
