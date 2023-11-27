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


def delete_text_review_markup():
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