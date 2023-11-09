import telebot
from telebot import types

Token = '6885108099:AAHklPS9V1WDWps8zxWK1I7CP_upFyMknTY'
bot = telebot.TeleBot(Token)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

@bot.message_handler(commands=['start'])
def choosesubject(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Математика")
    btn2 = types.KeyboardButton("Физика")
    btn3 = types.KeyboardButton("История")
    btn4 = types.KeyboardButton("ОРГ")
    btn5 = types.KeyboardButton("ИТИС")
    btn6 = types.KeyboardButton("Английский язык")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, 'Здравствуйте, выберите предмет', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def chooseteacher(message):
    if (message.text == 'Математика'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        BtnShest = types.KeyboardButton("Шестакова")
        BtnBel = types.KeyboardButton("Белоусова")
        Btnback = types.KeyboardButton("Вернуться к выбору предмета")
        markup.add(BtnShest, BtnBel, Btnback)
        bot.send_message(message.chat.id, 'Выберите преподавателя, про которого вы хотите написать отзыв', reply_markup=markup)


    elif (message.text == "Вернуться к выбору предмета"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Математика")
        btn2 = types.KeyboardButton("Физика")
        btn3 = types.KeyboardButton("История")
        btn4 = types.KeyboardButton("ОРГ")
        btn5 = types.KeyboardButton("ИТИС")
        btn6 = types.KeyboardButton("Английский язык")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, text="Вы вернулись к выбору предмета", reply_markup=markup)


    if (message.text == 'Шестакова'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Btnback = types.KeyboardButton("Вернуться к выбору преподавателя")
        markup.add(Btnback)
        bot.send_message(message.chat.id, 'Напишите отзыв', reply_markup=markup)

    elif (message.text == "Вернуться к выбору преподавателя"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        BtnShest = types.KeyboardButton("Шестакова")
        BtnBel = types.KeyboardButton("Белоусова")
        Btnback = types.KeyboardButton("Вернуться к выбору предмета")
        markup.add(BtnShest, BtnBel, Btnback)
        bot.send_message(message.chat.id, 'Выберите преподавателя, про которого вы хотите написать отзыв', reply_markup=markup)






bot.polling()
