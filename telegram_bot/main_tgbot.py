import logging
import telebot
from telebot import types
import handlers
import markups
import db_func
import os

from dotenv import load_dotenv
load_dotenv()


bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'Приветствую тебя в нашем боте!\nНиже тебе доступны команды',
                     reply_markup=markups.start_markup())
    db_func.create_text_reviews_db()   # create table
    db_func.create_rating_reviews_db()   # create table


@bot.message_handler(content_types=['text'])
def text_input(message):
    my_handlers = handlers.MyHandlers(bot)
    reviews = handlers.Reviews(bot)
    if message.text.lower() == 'составить расписание':
        db_func.create_modeus_db()
        my_handlers.check_modeus_status(message)
    elif message.text.lower() == 'отзывы':
        bot.send_message(message.chat.id, 'В этом разделе вы можете взаимодействовать с отзывами',
                         reply_markup=markups.first_step_reviews_markup())
        bot.register_next_step_handler(message, reviews.check_first_step_text_reviews)
    elif message.text.lower() == 'назад':
        start(message)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю о чём вы')


if __name__ == '__main__':
    bot.polling(none_stop=True)
