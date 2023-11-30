import os

relative_path = "telegram_bot/main_tgbot.py"
absolute_path = os.path.abspath(relative_path)
print(absolute_path)

absolute_project_path = os.path.dirname(os.path.abspath("Modeus_scheduler"))
print(absolute_project_path)

# C:\Program Files\PostgreSQL\16\bin

# "C:\Program Files\PostgreSQL\16\bin\pg_config.exe"

# python setup.py build_ext --pg-config C:\Program Files\PostgreSQL\16\bin\pg_config.exe build
