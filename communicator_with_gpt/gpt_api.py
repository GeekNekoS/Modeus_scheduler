from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
# from table_processing import when_study

with open("table.txt", "r", encoding="utf-8") as table:
    math = table.read()
# with open("other_table.txt", "r") as o_table:
#     physics = o_table.read()

client = OpenAI(
    api_key=os.getenv("KEY1"),
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
                {
                    "role": "system",
                    "content": math
                        +"""Each row contains information about the study team's classes for the week
        In each row the elements are separated by a comma:
        The first element of the row is Study Team.
        The second element of the row is the Training subject.
        The next elements in brackets are the classes that take place during the week for the team in the same row .
        Each lesson is specified in the format - (Day_of_week,Time_beginning,Time_end,Teacher).
        The line of information about the team's lessons ends with a dot.
        Your task is to write which team is suitable for the user, if there is no suitable command, you should answer that there is no suitable command."""
                },
                {
                    "role": "user",
                    "content": "Без занятий в субботу"
                }
             ],
    n=1,
    temperature=0
)

chat_response = completion.choices[0].message.content
print(chat_response)
