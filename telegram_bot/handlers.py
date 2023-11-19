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
            db_func.teacher_now(message.text.lower(), message.from_user.id)
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
            main_tgbot.start(message)
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
            if len(review_info) != 0:
                text = f'Преподаватель:\n{teacher.text.upper()}\n\n\n'
                for i in range(len(review_info)):
                    text += str(review_info[i][0]) + '\n\n'
                print(text)
                self.bot.send_message(teacher.chat.id, text, reply_markup=markups.reviews_markup())
            else:
                self.bot.send_message(teacher.chat.id, 'Сейчас нет отзывов об этом преподавателе!\nОставь первый)',
                                      reply_markup=markups.reviews_markup())
        else:
            self.bot.send_message(teacher.chat.id, 'Неверное имя преподавателя\nУкажите другое')
            self.bot.register_next_step_handler(teacher, self.find_review_text)
