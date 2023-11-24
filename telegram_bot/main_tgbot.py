import logging
import telebot
from telebot import types
import handlers
import markups
import db_func

TOKEN = "6417309065:AAFotgeFNidq8gg-T7fDxLfI3j91wXKM2FM"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'Приветствую тебя в нашем боте!\nНиже тебе доступны команды',
                     reply_markup=markups.start_markup())
    db_func.create_text_reviews_db()  # create table


@bot.message_handler(content_types=['text'])
def text_input(message):
    my_handlers = handlers.MyHandlers(bot)
    if message.text.lower() == 'составить расписание':
        db_func.create_modeus_db()
        my_handlers.check_modeus_status(message)
    elif message.text.lower() == 'отзывы':
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
