import os

relative_path = "telegram_bot/main_tgbot.py"
absolute_path = os.path.abspath(relative_path)
print(absolute_path)

absolute_project_path = os.path.dirname(os.path.abspath("Modeus_scheduler"))
print(absolute_project_path)
