from telebot import types


def start_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Составить расписание')
    btn2 = types.KeyboardButton('Отзывы')
    markup.add(btn1)
    markup.add(btn2)

    return markup


def second_step_reviews_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Смотреть отзывы')
    btn2 = types.KeyboardButton('Оставить отзыв')
    btn3 = types.KeyboardButton('Назад')
    markup.add(btn1, btn2)
    markup.add(btn3)

    return markup


def first_step_reviews_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Текстовые отзывы')
    btn2 = types.KeyboardButton('Рейтинговые отзывы')
    btn3 = types.KeyboardButton('Назад')
    markup.add(btn1, btn2)
    markup.add(btn3)

    return markup


def modeus_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Приступить к созданию')
    btn2 = types.KeyboardButton('Выйти из аккаунта')
    btn3 = types.KeyboardButton('Назад')
    markup.add(btn1, btn2)
    markup.add(btn3)

    return markup


def delete_review_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Удалить этот отзыв')
    btn2 = types.KeyboardButton('Назад')

    markup.add(btn1)
    markup.add(btn2)

    return markup


def back_to_start_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    return markup


def rating_reviews_markup(teacher_name):
    inline_markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text='1', callback_data='1*'+teacher_name)
    btn2 = types.InlineKeyboardButton(text='2', callback_data='2*'+teacher_name)
    btn3 = types.InlineKeyboardButton(text='3', callback_data='3*'+teacher_name)
    btn4 = types.InlineKeyboardButton(text='4', callback_data='4*'+teacher_name)
    btn5 = types.InlineKeyboardButton(text='5', callback_data='5*'+teacher_name)

    inline_markup.add(btn1, btn2, btn3, btn4, btn5)

    return inline_markup
