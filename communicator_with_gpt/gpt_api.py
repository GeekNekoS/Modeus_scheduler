from openai import OpenAI
# from table_processing import when_study

with open("table.txt", "r", encoding="utf-8") as table:
    math = table.read()
with open("other_table.txt", "r") as o_table:
    physics = o_table.read()


#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
#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
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

# sys = open("sys.txt", "r")
# sys_message = sys.read()
# sys.close()
completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
                {
                    "role": "system",
                    "content": "Твоя задача из таблицы ниже  выбрать команду, которая будет удовлетворять желаниям пользователя\n"
                               + math
                },
                {
                    "role": "user",
                    "content": "Хочу, чтобы занятия имели минимальный временной промежуток между друг другом"
                }
             ],
    n=1
)

chat_response = completion.choices[0].message.content
print(chat_response)
