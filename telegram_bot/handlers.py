import main_tgbot
import db_func
import markups


class MyHandlers:
    def __init__(self, bot):
        self.bot = bot

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
            self.bot.register_next_step_handler(message, self.check_next_step_modeus)

    def enter_modeus_login(self, message):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.enter_modeus_login)
        elif message.text.lower() == 'назад':
            main_tgbot.start(message)
        else:
            self.bot.send_message(message.chat.id, 'Введите ваш пароль:')
            self.bot.register_next_step_handler(message, self.add_login_and_password_to_db, message.text)

    def add_login_and_password_to_db(self, user_password, user_login):
        if not isinstance(user_password.text, str):
            self.bot.send_message(user_password.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(user_password, self.add_login_and_password_to_db, user_login)
        elif user_password.text.lower() == 'назад':
            main_tgbot.start(user_password)
        else:
            db_func.reg_user_in_modeus(user_password.from_user.id, user_login, user_password.text)
            self.bot.send_message(user_password.chat.id, 'Вы успешно вошли в аккаунт!',
                                  reply_markup=markups.modeus_markup())
            self.bot.register_next_step_handler(user_password, self.check_next_step_modeus)

    def check_next_step_modeus(self, message):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.check_next_step_modeus)
        elif message.text.lower() == 'назад':
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
            self.bot.register_next_step_handler(message, self.check_next_step_modeus)

    def add_user_preference(self, message):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.add_user_preference)
        elif message.text.lower() == 'назад':
            self.bot.send_message(message.chat.id, 'В этом разделе вы можете составить расписание,'
                                                   ' исходя из ваших пожеланий',
                                  reply_markup=markups.modeus_markup())
            self.bot.register_next_step_handler(message, self.check_next_step_modeus)
        else:
            self.bot.send_message(message.chat.id, 'Начинаю создание вариантов вашего расписания...',
                                  reply_markup=markups.start_markup())
            db_func.update_user_modeus_preference(message.text, message.from_user.id)


class Reviews:
    def __init__(self, bot):
        self.bot = bot

    def check_first_step_text_reviews(self, message):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.check_first_step_text_reviews)
        elif message.text.lower() == 'назад':
            main_tgbot.start(message)
        elif message.text.lower() == 'текстовые отзывы':
            self.bot.send_message(message.chat.id, 'В этом разделе вы можете взаимодействовать с текстовыми отзывами',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_second_step_text_reviews, message.text.lower())
        elif message.text.lower() == 'рейтинговые отзывы':
            self.bot.send_message(message.chat.id, 'В этом разделе вы можете взаимодействовать с рейтинговыми отзывами',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_second_step_text_reviews, message.text.lower())
        else:
            self.bot.send_message(message.chat.id, 'Не понимаю о чём вы')
            self.bot.register_next_step_handler(message, self.check_first_step_text_reviews)

    def check_second_step_text_reviews(self, message, command):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.check_second_step_text_reviews, command)
        elif message.text.lower() == 'назад':
            self.bot.send_message(message.chat.id, 'В этом разделе вы можете взаимодействовать с отзывами',
                                  reply_markup=markups.first_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_first_step_text_reviews)
        elif message.text.lower() == 'смотреть отзывы':
            self.bot.send_message(message.chat.id, 'Какой преподаватель вас интересует? ( ФИО )',
                                  reply_markup=markups.back_to_start_markup())
            if command == 'текстовые отзывы':
                self.bot.register_next_step_handler(message, self.get_text_review, command)
            else:
                # Здесь будет реализация рейтинговых отзывов
                pass
        elif message.text.lower() == 'оставить отзыв':
            self.bot.send_message(message.chat.id, 'Какой преподаватель вас интересует? ( ФИО )',
                                  reply_markup=markups.back_to_start_markup())
            if command == 'текстовые отзывы':
                self.bot.register_next_step_handler(message, self.enter_teacher_name_to_create_text_review, command)
            else:
                # Здесь будет реализация рейтинговых отзывов
                pass
        else:
            self.bot.send_message(message.chat.id, 'Не понимаю о чём вы')
            self.bot.register_next_step_handler(message, self.check_second_step_text_reviews, command)

    def get_text_review(self, teacher, command):
        if not isinstance(teacher.text, str):
            self.bot.send_message(teacher.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(teacher, self.get_text_review, command)
        elif teacher.text.lower() == 'назад':
            self.bot.send_message(teacher.chat.id, 'В этом разделе вы можете взаимодействовать с текстовыми отзывами',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(teacher, self.check_second_step_text_reviews, command)
        elif db_func.find_teacher(teacher.text.lower()):
            review_info = db_func.get_reviews_this_teacher(teacher.text.lower())
            text = f'Преподаватель:\n{teacher.text.upper()}\n\n\n'
            if len(review_info) != 0:
                for i in range(len(review_info)):
                    text += str(review_info[i][0]) + '\n\n'
                self.bot.send_message(teacher.chat.id, text, reply_markup=markups.second_step_reviews_markup())
            else:
                self.bot.send_message(teacher.chat.id, 'Сейчас нет отзывов об этом преподавателе!\nОставьте первый)',
                                      reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(teacher, self.check_second_step_text_reviews, command)
        else:
            self.bot.send_message(teacher.chat.id, 'Неверное имя преподавателя\nУкажите другое')
            self.bot.register_next_step_handler(teacher, self.get_text_review, command)

    def enter_teacher_name_to_create_text_review(self, message, command):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.enter_teacher_name_to_create_text_review, command)
        elif message.text.lower() == 'назад':
            self.bot.send_message(message.chat.id, 'В этом разделе вы можете взаимодействовать с текстовыми отзывами',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_second_step_text_reviews, command)
        elif db_func.find_teacher(message.text.lower()):
            if db_func.check_with_text_review(message.text.lower(), message.from_user.id):
                text = ('Отлично!\nТеперь расскажите, какое у вас мнение сложилось об этом преподавателе\n'
                        'Постарайтесь аргументировать свою позицию')
                self.bot.send_message(message.chat.id, text, reply_markup=markups.back_to_start_markup())
                self.bot.register_next_step_handler(message, self.create_text_review, message.text.lower(), command)
            else:
                self.bot.send_message(message.chat.id, 'Вы уже оставили отзыв на этого преподавателя',
                                      reply_markup=markups.delete_text_review_markup())
                self.bot.register_next_step_handler(message, self.check_third_step_text_reviews, message.text.lower(),
                                                    command)
        else:
            self.bot.send_message(message.chat.id, 'Неверное имя преподавателя\nУкажите другое')
            self.bot.register_next_step_handler(message, self.enter_teacher_name_to_create_text_review, command)

    def create_text_review(self, review, teacher, command):
        if not isinstance(review.text, str):
            self.bot.send_message(review.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(review, self.create_text_review, teacher, command)
        elif review.text.lower() == 'назад':
            self.bot.send_message(review.chat.id, 'В этом разделе вы можете взаимодействовать с текстовыми отзывами',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(review, self.check_second_step_text_reviews, command)
        else:
            db_func.review_creator(review.from_user.id, teacher, review.text)
            self.bot.send_message(review.chat.id, 'Ваш отзыв зарегистрирован!',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(review, self.check_second_step_text_reviews, command)

    def check_third_step_text_reviews(self, message, teacher_name, command):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.check_third_step_text_reviews, teacher_name, command)
        elif message.text.lower() == 'назад':
            self.bot.send_message(message.chat.id, 'В этом разделе вы можете взаимодействовать с текстовыми отзывами',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_second_step_text_reviews, command)
        elif message.text.lower() == 'удалить этот отзыв':
            db_func.delete_text_review(message.from_user.id, teacher_name)
            self.bot.send_message(message.chat.id, 'Удалено!', reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_second_step_text_reviews, command)
        else:
            self.bot.send_message(message.chat.id, 'Не понимаю о чём вы')
            self.bot.register_next_step_handler(message, self.check_third_step_text_reviews, teacher_name, command)
