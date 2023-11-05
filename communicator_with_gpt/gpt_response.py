import g4f
from table_processing import when_study


table = when_study("table.txt")
other_table = when_study("other_table.txt")


response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
 #   provider=g4f.Provider.GeekGpt,
    messages=[{"role": "user",
               "content": "Математика\n"
                          + table
                          + "Физика\n"
                          + other_table
                          + "Я не хочу заниматься математикой в субботу и не хочу лекцию по физике во вторник, какие учебные команды мне выбрать? "}],
    stream=True,
    temperature = 0
)

for message in response:
    print(message, flush=True, end='')