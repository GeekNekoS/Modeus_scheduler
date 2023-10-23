import logging
import telebot
from telebot import types


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "6417309065:AAFotgeFNidq8gg-T7fDxLfI3j91wXKM2FM"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, """
    Доступные команды:
    /hello
    # /learn_the_safety_rules_in_the_gym
    # /leave_a_review_about_the_teacher
    """)


@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, "Привет, чё как?")


#
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


#
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)


