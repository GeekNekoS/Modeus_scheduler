from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
from communicator_with_gpt.table_from_database import create_table_file


def create_personal_schedule(user_id):
    # Создание текстового файла по базе данных для запроса к GPT
    create_table_file(user_id)

    with open("output_table.txt", "r", encoding="utf-8") as o_table:
          table = o_table.read()

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
                            В каждой строке элементы разделяются символом /:
                            Первый элемент строки — Учебная команда.
                            Второй элемент строки – Учебный предмет.
                            Следующие элементы в скобках — это занятия, которые проводятся в течение недели для команды в той же строке.
                            Каждый урок указывается в формате: (День недели,Время проведения).
                            Строка информации о занятиях команды заканчивается точкой.
                            Ваша задача написать какая команда подходит пользователю, если подходящей команды нет, следует ответить, что подходящей команды нет.\n"""
                        + table
                    },
                    {
                        "role": "user",
                        "content": "Занятия по английскому в пятницу после 12:00"
                                   "В ответе напиши только команду"
                    }
                 ],
        n=1,
        temperature=0
    )

    chat_response = completion.choices[0]
    return chat_response.message.content
