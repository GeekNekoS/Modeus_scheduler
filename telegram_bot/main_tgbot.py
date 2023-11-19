import logging
import telebot
from telebot import types
import handlers
# from handlers import MyHandlers
import markups
import db_func
import sqlite3

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

TOKEN = "6417309065:AAFotgeFNidq8gg-T7fDxLfI3j91wXKM2FM"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'Приветствую тебя в нашем боте!\nНиже тебе доступны команды',
                     reply_markup=markups.start_markup())
    db_func.reg()
    db_func.reg_reviews()
    if not db_func.is_user(message.from_user.id):
        db_func.add(message.from_user.id)


@bot.message_handler(content_types=['text'])
def text_input(message):
    my_handlers = handlers.MyHandlers(bot)
    if message.text.lower() == 'составить расписание':
        # db_func.set_activity_status0(message.from_user.id)
        bot.send_message(message.chat.id, 'Необходимо войти в вашу учетную запись,'
                                          ' для получения информации о доступных вам дисциплинах',
                         reply_markup=markups.back_to_start_markup())
        bot.send_message(message.chat.id, 'Введите ваш логин: ')
    elif message.text.lower() == 'отзывы':
        # db_func.set_activity_status0(message.from_user.id)
        bot.send_message(message.chat.id, 'Выберите, что именно вас интересует',
                         reply_markup=markups.reviews_markup())
    elif message.text.lower() == 'оставить отзыв':
        bot.send_message(message.chat.id, 'Введите имя преподавателя',
                         reply_markup=markups.back_to_start_markup())
        bot.register_next_step_handler(message, my_handlers.enter_teacher_name)
    elif message.text.lower() == 'смотреть отзывы':
        bot.send_message(message.chat.id, 'Какой преподаватель вас интересует? ( ФИО )',
                         reply_markup=markups.back_to_start_markup())
        bot.register_next_step_handler(message, my_handlers.find_review_text)
    elif message.text.lower() == 'назад в меню':
        start(message)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю о чём вы')


if __name__ == '__main__':
    bot.polling(none_stop=True)
