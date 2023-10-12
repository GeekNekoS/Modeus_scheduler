import logging
import telebot
import os


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "6417309065:AAFotgeFNidq8gg-T7fDxLfI3j91wXKM2FM"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, 'В стадии разработки')


if __name__ == '__main__':
    bot.polling(none_stop=True)
