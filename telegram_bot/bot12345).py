import logging
import telebot
from telebot import types

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "6417309065:AAFotgeFNidq8gg-T7fDxLfI3j91wXKM2FM"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Старт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Привет')
    btn3 = types.KeyboardButton('Помощь')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id,
                     f'Приветствую тебя в нашем боте!\nНиже тебе доступны команды',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_input(message):
    if message.text.lower() == 'старт':
        bot.send_message(message.chat.id, """
    Доступные команды:
    /hello
    # /learn_the_safety_rules_in_the_gym
    # /leave_a_review_about_the_teacher
    """)
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, чё как?')
    if message.text.lower() == 'помощь':
        bot.send_message(message.chat.id, 'Бог в помощь')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)