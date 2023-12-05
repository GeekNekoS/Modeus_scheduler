import os

relative_path = "dir_path.py"
absolute_path = os.path.dirname(os.path.abspath(relative_path))
print(absolute_path)

# absolute_project_path = os.path.dirname(os.path.abspath("Modeus_scheduler"))
# print(absolute_project_path)
