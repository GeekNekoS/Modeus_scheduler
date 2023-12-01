from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


with open("table_math_optimised.txt", "r", encoding="utf-8") as table:
    math = table.read()

with open("table_physic_optimised.txt", "r") as o_table:
     physics = o_table.read()

client = OpenAI(
    api_key=os.getenv("KEY_OPENAI"),
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
                {
                    "role": "system",
                    "content":
                        """В каждой строке содержится информация о занятиях учебной команды на неделе.
                        В каждой строке элементы разделяются запятой:
                        Первый элемент строки — Учебная команда.
                        Второй элемент строки – Учебный предмет.
                        Следующие элементы в скобках — это занятия, которые проводятся в течение недели для команды в той же строке.
                        Каждый урок указывается в формате: (День недели,Время начала,Время окончания,Учитель).
                        Строка информации о занятиях команды заканчивается точкой.
                        Ваша задача написать какая команда подходит пользователю, если подходящей команды нет, следует ответить, что подходящей команды нет.\n"""
                    + math
                    + physics
                },
                {
                    "role": "user",
                    "content": "Скомбинируй две команды по физике и математике так, чтобы занятия не пересекались"
                               "В ответе напиши только команды"
                }
             ],
    n=1,
    temperature=0
)

chat_response = completion.choices
for i in chat_response:
    print(i.message.content)
