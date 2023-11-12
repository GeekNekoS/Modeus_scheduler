from telebot import types


def start_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Старт')
    btn2 = types.KeyboardButton('Привет')
    btn3 = types.KeyboardButton('Помощь')
    btn4 = types.KeyboardButton('Техника безопасности')
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)

    return markup


def safety_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Смотреть правила')
    btn2 = types.KeyboardButton('Мой прогресс')
    btn3 = types.KeyboardButton('Назад в меню')

    markup.add(btn1, btn2)
    markup.add(btn3)

    return markup
