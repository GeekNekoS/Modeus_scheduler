from schedules_parsing.tasks.create_and_fill_lessons_table import create_and_fill_lessons_table
from schedules_parsing.tasks.create_and_fill_directions_table import create_and_fill_directions_table
from schedules_parsing.tasks.create_and_fill_schedules_table import create_and_fill_schedules_table

from work_with_db_draft.fill_schedules_tables import main as fill_schedules_tables  #


if __name__ == "__main__":
    create_and_fill_lessons_table()
    create_and_fill_directions_table()
    # create_and_fill_schedules_table()

    fill_schedules_tables()
