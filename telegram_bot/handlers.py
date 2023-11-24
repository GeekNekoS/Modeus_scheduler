import main_tgbot
import db_func
import markups


class MyHandlers:
    def __init__(self, bot):
        self.bot = bot

    def enter_teacher_name(self, message):
        with open('teachers.txt', encoding='utf-8') as f:
            teachers = f.read().lower().split('\n')
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.enter_teacher_name)
        elif message.text.lower() == 'назад в меню':
            main_tgbot.start(message)
        elif message.text.lower() in teachers:
            text = ('Отлично!\nТеперь расскажите, какое у вас мнение сложилось об этом преподавателе\n'
                    'Постарайтесь аргументировать свою позицию')
            self.bot.send_message(message.chat.id, text, reply_markup=markups.back_to_start_markup())
            self.bot.register_next_step_handler(message, self.create_review, message.text.lower())
        else:
            self.bot.send_message(message.chat.id, 'Неверное имя преподавателя\nУкажите другое')
            self.bot.register_next_step_handler(message, self.enter_teacher_name)

    def create_review(self, review, teacher):
        if not isinstance(review.text, str):
            self.bot.send_message(review.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(review, self.create_review, teacher)
        elif review.text.lower() == 'назад в меню':
            main_tgbot.start(review)
        else:
            db_func.review_creator(teacher, review.text)
            self.bot.send_message(review.chat.id, 'Ваш отзыв зарегистрирован!',
                                  reply_markup=markups.reviews_markup())

    def find_review_text(self, teacher):
        with open('teachers.txt', encoding='utf-8') as f:
            teachers = f.read().lower().split('\n')
        if not isinstance(teacher.text, str):
            self.bot.send_message(teacher.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(teacher, self.find_review_text)
        elif teacher.text.lower() == 'назад в меню':
            main_tgbot.start(teacher)
        elif teacher.text.lower() in teachers:
            review_info = db_func.get_reviews_this_teacher(teacher.text.lower())
            text = f'Преподаватель:\n{teacher.text.upper()}\n\n\n'
            if len(review_info) != 0:
                for i in range(len(review_info)):
                    text += str(review_info[i][0]) + '\n\n'
                self.bot.send_message(teacher.chat.id, text, reply_markup=markups.reviews_markup())
            else:
                self.bot.send_message(teacher.chat.id, 'Сейчас нет отзывов об этом преподавателе!\nОставь первый)',
                                      reply_markup=markups.reviews_markup())
        else:
            self.bot.send_message(teacher.chat.id, 'Неверное имя преподавателя\nУкажите другое')
            self.bot.register_next_step_handler(teacher, self.find_review_text)

    def check_modeus_status(self, message):
        if not db_func.is_user_login_modeus(message.from_user.id):
            self.bot.send_message(message.chat.id, 'Необходимо войти в вашу учетную запись,'
                                                   ' для получения информации о доступных вам дисциплинах',
                                  reply_markup=markups.back_to_start_markup())
            self.bot.send_message(message.chat.id, 'Введите ваш логин: ')
            self.bot.register_next_step_handler(message, self.enter_modeus_login)
        else:
            self.bot.send_message(message.chat.id, 'Вы уже вошли в аккаунт',
                                  reply_markup=markups.modeus_markup())
            self.bot.register_next_step_handler(message, self.check_next_step)

    def enter_modeus_login(self, message):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.enter_modeus_login)
        elif message.text.lower() == 'назад в меню':
            main_tgbot.start(message)
        else:
            self.bot.send_message(message.chat.id, 'Введите ваш пароль:')
            self.bot.register_next_step_handler(message, self.add_login_and_password_to_db, message.text)

    def add_login_and_password_to_db(self, user_password, user_login):
        if not isinstance(user_password.text, str):
            self.bot.send_message(user_password.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(user_password, self.add_login_and_password_to_db, user_login)
        elif user_password.text.lower() == 'назад в меню':
            main_tgbot.start(user_password)
        else:
            db_func.reg_user_in_modeus(user_password.from_user.id, user_login, user_password.text)
            self.bot.send_message(user_password.chat.id, 'Вы успешно вошли в аккаунт!',
                                  reply_markup=markups.modeus_markup())
            self.bot.register_next_step_handler(user_password, self.check_next_step)

    def check_next_step(self, message):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.check_next_step)
        elif message.text.lower() == 'назад в меню':
            main_tgbot.start(message)
        elif message.text.lower() == 'выйти из аккаунта':
            db_func.leave_modeus_account(message.from_user.id)
            self.bot.send_message(message.chat.id, 'Вы вышли из аккаунта',
                                  reply_markup=markups.start_markup())
        elif message.text.lower() == 'приступить к созданию':
            self.bot.send_message(message.chat.id, 'Введите свои пожелания к расписанию',
                                  reply_markup=markups.back_to_start_markup())
            self.bot.register_next_step_handler(message, self.add_user_preference)
        else:
            self.bot.send_message(message.chat.id, 'Не понимаю о чём вы')
            self.bot.register_next_step_handler(message, self.check_next_step)

    def add_user_preference(self, message):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.add_user_preference)
        else:
            self.bot.send_message(message.chat.id, 'Начинаю создание вариантов вашего расписания...',
                                  reply_markup=markups.start_markup())
            db_func.update_user_modeus_preference(message.text, message.from_user.id)
