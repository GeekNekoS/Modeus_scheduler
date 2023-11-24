from telebot import types


def start_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Составить расписание')
    # btn2 = types.KeyboardButton('Привет')
    btn3 = types.KeyboardButton('Отзывы')
    # btn4 = types.KeyboardButton('Техника безопасности')
    markup.add(btn1)
    markup.add(btn3)

    return markup


def safety_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Смотреть правила')
    btn2 = types.KeyboardButton('Мой прогресс')
    btn3 = types.KeyboardButton('Назад в меню')

    markup.add(btn1, btn2)
    markup.add(btn3)

    return markup


def reviews_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Смотреть отзывы')
    btn2 = types.KeyboardButton('Оставить отзыв')
    btn3 = types.KeyboardButton('Назад в меню')
    markup.add(btn1, btn2)
    markup.add(btn3)

    return markup


def back_to_start_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Назад в меню')
    markup.add(btn1)

    return markup


def modeus_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Приступить к созданию')
    btn2 = types.KeyboardButton('Выйти из аккаунта')
    btn3 = types.KeyboardButton('Назад в меню')
    markup.add(btn1, btn2)
    markup.add(btn3)

    return markup
