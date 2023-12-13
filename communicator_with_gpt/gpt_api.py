from openai import OpenAI
from communicator_with_gpt.teachers_processing import get_avg_teacher_grades
from communicator_with_gpt.lessons_processing import get_user_lessons_table
import os

from dotenv import load_dotenv
load_dotenv()


KEY_OPENAI = os.getenv("KEY_OPENAI")


def create_personal_schedule(user_id, query):
    get_user_lessons_table(user_id)

    with open(f"temp_files\\schedule_{user_id}.txt", "r", encoding="utf-8") as o_table:
        table = o_table.read()

    with open("prompt.txt", "r", encoding="utf-8") as prompt_text:
        sys_prompt = prompt_text.read()

    client = OpenAI(api_key=KEY_OPENAI)

    query_prompt = ("Выбери по одной команде для каждого предмета, чтобы никакие занятия этих команд не "
                    "совпадали по времени проведения и дням недели. В ответ напиши только названия команд."
                    "Если есть такая возможность, то оценка преподавателя команды должна быть наивысшей\n")

    avg_teacher_grades = get_avg_teacher_grades()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": sys_prompt + table + avg_teacher_grades
            },
            {
                "role": "user",
                "content": query_prompt + query
            }
        ],
        n=1,
        temperature=0,
        max_tokens=600
    )

    chat_response = completion.choices[0]
    return chat_response.message.content
