import g4f
from table_processing import when_study


table = when_study()

response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": table + "Какие команды представлены?"}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')