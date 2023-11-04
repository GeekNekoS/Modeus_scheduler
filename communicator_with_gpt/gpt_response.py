import g4f
from table_processing import when_study


table = when_study()

response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    provider=g4f.Provider.GeekGpt,
    messages=[{"role": "user",
               "content": table + "Какую команду мне выбрать, если не хочу учиться в субботу?"}],
    stream=True,
    temperature = 1.9
)

for message in response:
    print(message, flush=True, end='')