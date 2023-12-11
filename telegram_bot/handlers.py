import time
import __main__
import db_func
import markups
from communicator_with_gpt.gpt_api import *
from parsing.schedules.login import is_user_logedin_modeus
from parsing.schedules.parse_schedules_data import create_and_fill_schedules_table


class MyHandlers:
    def __init__(self, bot):
        self.bot = bot

    def check_modeus_status(self, message):
        if db_func.if_table_schedule_exists(message.from_user.id):
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
            if is_user_logedin_modeus(user_login, user_password.text):
                self.bot.send_message(user_password.chat.id, 'Вы успешно вошли в аккаунт!')
                self.bot.send_message(user_password.chat.id, 'Начинаю парсинг доступных вам дисциплин...',
                                      reply_markup=None)
                # Тут старт парсера, при этом таблицы users_modeus не существует,
                # т.е. логин и пароль передаются на этом моменте
                # create_and_fill_db(message.from_user.id)

                try:
                    start = time.perf_counter()
                    create_and_fill_schedules_table(user_login, user_password.text, user_password.chat.id)
                    stop = time.perf_counter()
                    print(f"Программа выполняется за {stop - start} секунд")
                except Exception as ex:
                    print(ex)
                    self.bot.send_message(user_password.chat.id, 'Парсер пока не переведён в режим headless. Сбор информации приостановлен')

                self.bot.send_message(user_password.chat.id, 'Парсинг завершён успешно',
                                      reply_markup=markups.modeus_markup())
                self.bot.register_next_step_handler(user_password, self.check_next_step_modeus)
            else:
                self.bot.send_message(user_password.chat.id, 'Неверный логин или пароль',
                                      reply_markup=markups.back_to_start_markup())
                self.bot.register_next_step_handler(user_password, self.check_modeus_status)

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
            # drop_table(f"schedules_{message.chat.id}")  # <== Nekos
        elif message.text.lower() == 'приступить к созданию':
            self.bot.send_message(message.chat.id, 'Введите ваши пожелания к расписанию')
            self.bot.register_next_step_handler(message, self.add_user_preference)
            # self.bot.send_message(message.chat.id, 'Введите пароль от Modeus для начала парсинга',
            #                       reply_markup=markups.back_to_start_markup())
            # self.bot.register_next_step_handler(message, self.enter_user_password_2)
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
            self.bot.send_message(message.chat.id, 'Начало составления расписания...',
                                  reply_markup=markups.start_markup())
            self.average_rating_reviews()
            # Тут Кеше передаются аргументы для создания расписания
            answer = create_personal_schedule(message.from_user.id, message.text)
            self.bot.send_message(message.chat.id, answer,
                                  reply_markup=markups.start_markup())

    def average_rating_reviews(self):
        db_func.rating_review_table_helper_dropper_all()
        db_func.rating_review_table_helper_creator()
        review_info = db_func.get_all_rating_reviews()
        # print(review_info)
        for i in range(len(review_info)):
            review_this_teacher = db_func.rating_review_table_helper_getter(review_info[i][1])
            if len(review_this_teacher) == 0:
                db_func.rating_review_table_helper_setter(review_info[i][1], review_info[i][2], review_info[i][3],
                                                          review_info[i][4], review_info[i][5], review_info[i][6],
                                                          review_info[i][7], review_info[i][8], review_info[i][9],
                                                          review_info[i][10], review_info[i][11])
            else:
                new_average = [review_info[i][1]]
                for j in range(2, 12):
                    new_data = str(review_info[i][j])+str(review_this_teacher[0][j-1])
                    new_average.append(new_data)
                db_func.rating_review_table_helper_dropper(review_info[i][1])
                db_func.rating_review_table_helper_setter(new_average[0], new_average[1], new_average[2],
                                                          new_average[3], new_average[4], new_average[5],
                                                          new_average[6], new_average[7], new_average[8],
                                                          new_average[9], new_average[10])
        db_func.average_rating_reviews_dropper()
        all_helper = db_func.get_all_rating_reviews_helper()
        for i in range(len(all_helper)):
            new_average = [all_helper[i][0]]
            for j in range(1, 11):
                this_data = str(all_helper[i][j]).replace('0','')
                if len(this_data) == 0:
                    new_average.append(0)
                else:
                    summ = 0
                    for el in this_data:
                        summ += int(el)
                    new_average.append(summ/len(this_data))
            db_func.average_rating_reviews_creator()
            db_func.average_rating_reviews_setter(new_average[0], new_average[1], new_average[2], new_average[3],
                                                  new_average[4], new_average[5], new_average[6], new_average[7],
                                                  new_average[8], new_average[9], new_average[10])


class Reviews:
    def __init__(self, bot):
        self.bot = bot

    def check_first_step_all_reviews(self, message):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.check_first_step_all_reviews)
        elif message.text.lower() == 'назад':
            main_tgbot.start(message)
        elif message.text.lower() == 'текстовые отзывы':
            self.bot.send_message(message.chat.id, 'В этом разделе вы можете взаимодействовать с текстовыми отзывами',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_second_step_all_reviews, message.text.lower())
        elif message.text.lower() == 'рейтинговые отзывы':
            self.bot.send_message(message.chat.id, 'В этом разделе вы можете взаимодействовать с рейтинговыми отзывами',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_second_step_all_reviews, message.text.lower())
        else:
            self.bot.send_message(message.chat.id, 'Не понимаю о чём вы')
            self.bot.register_next_step_handler(message, self.check_first_step_all_reviews)

    def check_second_step_all_reviews(self, message, command):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.check_second_step_all_reviews, command)
        elif message.text.lower() == 'назад':
            self.bot.send_message(message.chat.id, 'В этом разделе вы можете взаимодействовать с отзывами',
                                  reply_markup=markups.first_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_first_step_all_reviews)
        elif message.text.lower() == 'смотреть отзывы':
            self.bot.send_message(message.chat.id, 'Какой преподаватель вас интересует? ( ФИО )',
                                  reply_markup=markups.back_to_start_markup())
            if command == 'текстовые отзывы':
                self.bot.register_next_step_handler(message, self.get_text_review, command)
            else:
                self.bot.register_next_step_handler(message, self.get_rating_review, command)
        elif message.text.lower() == 'оставить отзыв':
            self.bot.send_message(message.chat.id, 'Какой преподаватель вас интересует? ( ФИО )',
                                  reply_markup=markups.back_to_start_markup())
            if command == 'текстовые отзывы':
                self.bot.register_next_step_handler(message, self.enter_teacher_name_to_create_text_review, command)
            else:
                self.bot.register_next_step_handler(message, self.enter_teacher_name_to_create_rating_review, command)
        else:
            self.bot.send_message(message.chat.id, 'Не понимаю о чём вы')
            self.bot.register_next_step_handler(message, self.check_second_step_all_reviews, command)

    def get_text_review(self, teacher, command):
        if not isinstance(teacher.text, str):
            self.bot.send_message(teacher.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(teacher, self.get_text_review, command)
        elif teacher.text.lower() == 'назад':
            self.bot.send_message(teacher.chat.id, 'В этом разделе вы можете взаимодействовать с текстовыми отзывами',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(teacher, self.check_second_step_all_reviews, command)
        elif db_func.find_teacher(teacher.text.lower()):
            review_info = db_func.get_text_reviews_this_teacher(teacher.text.lower())
            text = f'Преподаватель:\n{teacher.text.upper()}\n\n\n'
            if len(review_info) != 0:
                for i in range(len(review_info)):
                    text += str(review_info[i][0]) + '\n\n'
                self.bot.send_message(teacher.chat.id, text, reply_markup=markups.second_step_reviews_markup())
            else:
                self.bot.send_message(teacher.chat.id, 'Сейчас нет отзывов об этом преподавателе!\nОставьте первый)',
                                      reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(teacher, self.check_second_step_all_reviews, command)
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
            self.bot.register_next_step_handler(message, self.check_second_step_all_reviews, command)
        elif db_func.find_teacher(message.text.lower()):
            if db_func.check_with_text_review(message.text.lower(), message.from_user.id):
                text = ('Отлично!\nТеперь расскажите, какое у вас мнение сложилось об этом преподавателе\n'
                        'Постарайтесь аргументировать свою позицию')
                self.bot.send_message(message.chat.id, text, reply_markup=markups.back_to_start_markup())
                self.bot.register_next_step_handler(message, self.create_text_review, message.text.lower(), command)
            else:
                self.bot.send_message(message.chat.id, 'Вы уже оставили отзыв на этого преподавателя',
                                      reply_markup=markups.delete_review_markup())
                self.bot.register_next_step_handler(message, self.check_third_step_all_reviews, message.text.lower(),
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
            self.bot.register_next_step_handler(review, self.check_second_step_all_reviews, command)
        else:
            db_func.text_review_creator(review.from_user.id, teacher, review.text)
            self.bot.send_message(review.chat.id, 'Ваш отзыв зарегистрирован!',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(review, self.check_second_step_all_reviews, command)

    def check_third_step_all_reviews(self, message, teacher_name, command):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.check_third_step_all_reviews, teacher_name, command)
        elif message.text.lower() == 'назад':
            if command == 'текстовые отзывы':
                self.bot.send_message(message.chat.id, 'В этом разделе вы можете '
                                                       'взаимодействовать с текстовыми отзывами',
                                      reply_markup=markups.second_step_reviews_markup())
            else:
                self.bot.send_message(message.chat.id,
                                      'В этом разделе вы можете взаимодействовать с рейтинговыми отзывами',
                                      reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_second_step_all_reviews, command)
        elif message.text.lower() == 'удалить этот отзыв':
            if command == 'текстовые отзывы':
                db_func.delete_text_review(message.from_user.id, teacher_name)
            else:
                db_func.delete_rating_review(message.from_user.id, teacher_name)
            self.bot.send_message(message.chat.id, 'Удалено!', reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_second_step_all_reviews, command)
        else:
            self.bot.send_message(message.chat.id, 'Не понимаю о чём вы')
            self.bot.register_next_step_handler(message, self.check_third_step_all_reviews, teacher_name, command)

    def enter_teacher_name_to_create_rating_review(self, message, command):
        if not isinstance(message.text, str):
            self.bot.send_message(message.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(message, self.enter_teacher_name_to_create_rating_review, command)
        elif message.text.lower() == 'назад':
            self.bot.send_message(message.chat.id, 'В этом разделе вы можете взаимодействовать с рейтинговыми отзывами',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(message, self.check_second_step_all_reviews, command)
        elif db_func.find_teacher(message.text.lower()):
            if db_func.check_with_rating_review(message.text.lower(), message.from_user.id):
                db_func.add_user_to_rating_db(message.from_user.id, message.text.lower())
                text = ('Супер!\nТеперь оцените преподавателя по представленным критериям, '
                        'где 1 - плохо, а 5 - отлично')
                self.bot.send_message(message.chat.id, text, reply_markup=markups.second_step_reviews_markup())
                self.bot.send_message(message.chat.id, 'Насколько доступно преподаватель объясняет материал?',
                                      reply_markup=markups.rating_reviews_markup(message.text.lower() + '*1'))
                self.bot.send_message(message.chat.id, 'Оцените его/её организацию и структуру урока',
                                      reply_markup=markups.rating_reviews_markup(message.text.lower() + '*2'))
                self.bot.send_message(message.chat.id, 'Какова его/её способность мотивировать студентов'
                                                       ' и создавать интерес к предмету?',
                                      reply_markup=markups.rating_reviews_markup(message.text.lower() + '*3'))
                self.bot.send_message(message.chat.id, 'Насколько эффективно преподаватель использует различные '
                                                       'методы обучения (лекции, семинары, практические задания и тд)?',
                                      reply_markup=markups.rating_reviews_markup(message.text.lower() + '*4'))
                self.bot.send_message(message.chat.id, 'Оцените его/её подход к оценке и обратной '
                                                       'связи по заданиям и экзаменам',
                                      reply_markup=markups.rating_reviews_markup(message.text.lower() + '*5'))
                self.bot.send_message(message.chat.id, 'Как преподаватель относится к вопросам и заботам студентов, '
                                                       'насколько хорошо отвечает на них?',
                                      reply_markup=markups.rating_reviews_markup(message.text.lower() + '*6'))
                self.bot.send_message(message.chat.id, 'Оцените, насколько хорошо занятия у этого '
                                                       'преподавателя развивают нужные вам навыки',
                                      reply_markup=markups.rating_reviews_markup(message.text.lower() + '*7'))
                self.bot.send_message(message.chat.id, 'Оцените доступность преподавателя, когда'
                                                       ' требуется дополнительная помощь',
                                      reply_markup=markups.rating_reviews_markup(message.text.lower() + '*8'))
                self.bot.send_message(message.chat.id, 'На ваш взгляд, насколько хорошо'
                                                       ' преподаватель знает свой предмет?',
                                      reply_markup=markups.rating_reviews_markup(message.text.lower() + '*9'))
                self.bot.send_message(message.chat.id, 'Насколько хорошо преподаватель понимает своих учеников?',
                                      reply_markup=markups.rating_reviews_markup(message.text.lower() + '*10'))
                self.bot.register_next_step_handler(message, self.check_second_step_all_reviews, command)
            else:
                self.bot.send_message(message.chat.id, 'Вы уже оставили отзыв на этого преподавателя',
                                      reply_markup=markups.delete_review_markup())
                self.bot.register_next_step_handler(message, self.check_third_step_all_reviews, message.text.lower(),
                                                    command)
        else:
            self.bot.send_message(message.chat.id, 'Неверное имя преподавателя\nУкажите другое')
            self.bot.register_next_step_handler(message, self.enter_teacher_name_to_create_rating_review, command)

    def get_rating_review(self, teacher, command):
        if not isinstance(teacher.text, str):
            self.bot.send_message(teacher.chat.id, 'Недоступный тип данных, введите текст')
            self.bot.register_next_step_handler(teacher, self.get_rating_review, command)
        elif teacher.text.lower() == 'назад':
            self.bot.send_message(teacher.chat.id, 'В этом разделе вы можете взаимодействовать с рейтинговыми отзывами',
                                  reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(teacher, self.check_second_step_all_reviews, command)
        elif db_func.find_teacher(teacher.text.lower()):
            review_info = db_func.get_rating_reviews_this_teacher(teacher.text.lower())
            # print(review_info)
            # text = f'Преподаватель:\n{teacher.text.upper()}\n\n\n'
            if len(review_info) != 0:
                text = self.counter_teacher_rating(teacher, review_info)
                self.bot.send_message(teacher.chat.id, text, reply_markup=markups.second_step_reviews_markup())
            else:
                self.bot.send_message(teacher.chat.id, 'Сейчас нет отзывов об этом преподавателе!\nОставьте первый)',
                                      reply_markup=markups.second_step_reviews_markup())
            self.bot.register_next_step_handler(teacher, self.check_second_step_all_reviews, command)
        else:
            self.bot.send_message(teacher.chat.id, 'Неверное имя преподавателя\nУкажите другое')
            self.bot.register_next_step_handler(teacher, self.get_rating_review, command)

    def counter_teacher_rating(self, teacher, review_info):
        dict_rating = {
            1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: ''
        }
        dict_criterion = {
            1: 'Насколько доступно преподаватель объясняет материал?',
            2: 'Оцените его/её организацию и структуру урока',
            3: 'Какова его/её способность мотивировать студентов и создавать интерес к предмету?',
            4: 'Насколько эффективно преподаватель использует различные методы обучения '
               '(лекции, семинары, практические задания и тд)?',
            5: 'Оцените его/её подход к оценке и обратной связи по заданиям и экзаменам',
            6: 'Как преподаватель относится к вопросам и заботам студентов, насколько хорошо отвечает на них?',
            7: 'Оцените, насколько хорошо занятия у этого преподавателя развивают нужные вам навыки',
            8: 'Оцените доступность преподавателя, когда требуется дополнительная помощь',
            9: 'На ваш взгляд, насколько хорошо преподаватель знает свой предмет?',
            10: 'Насколько хорошо преподаватель понимает своих учеников?'
        }
        text = f'Преподаватель:\n{teacher.text.upper()}\n\n\n\n'
        if len(review_info) == 1:
            for j in range(2, len(review_info[0])):
                dict_rating[j - 1] = str(review_info[0][j])
        else:
            for i in range(len(review_info) - 1):
                for j in range(2, len(review_info[0])):
                    dict_rating[j - 1] = str(review_info[i][j]) + str(review_info[i + 1][j])
        for i in range(1, 10 + 1):
            criterion = dict_rating[i].replace('0', '')
            if len(criterion) == 0:
                text += f'{dict_criterion[i]}\n\nСейчас нет ни одной оценки\n\n\n'
                continue
            sum_rating = 0
            for el in criterion:
                sum_rating += int(el)
            text += f'{dict_criterion[i]}\n\nРейтинг: {sum_rating / len(criterion)}, кол-во оценок: {len(criterion)}\n\n\n'
        return text
