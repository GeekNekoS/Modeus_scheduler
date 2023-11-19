import openai
from table_processing import when_study


table = when_study("table.txt")
other_table = when_study("other_table.txt")

openai.api_key = "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"
messages=[]

"""for i in range(2):
    content = input("User: ")
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    messages.append({"role": "assistant", "content": chat_response})"""


cont1 = "Математика\n" + table + "\nНазови команду или команды, которые не учатся в субботу?"
cont2 ="Физика\n" + other_table + "\nНазови команду или команды, котореы не учатся в понедельник?"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-1106",
    messages=[{"role": "user",
                "content": cont1},],
    n = 1,
    temperature = 0
)
chat_response = completion.choices[0].message.content
print(chat_response)
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-1106",
    messages=[{"role": "user",
                "content": cont2},],
    n = 1,
    temperature = 0
)
chat_response = completion.choices[0].message.content
print(chat_response)