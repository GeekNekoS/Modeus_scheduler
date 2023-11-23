from schedules_parsing_old_version.create_db_tables import create_db_tables
from schedules_parsing_old_version.fill_lessons_table import main as fill_lessons_table
from schedules_parsing_old_version.fill_directions_table import main as fill_directions_table
from schedules_parsing_old_version.fill_schedules_tables import main as fill_schedules_tables

import time


if __name__ == "__main__":
    start = time.perf_counter()

    create_db_tables()
    fill_lessons_table()
    fill_directions_table()
    fill_schedules_tables()

    stop = time.perf_counter()

    print(f"Выполнено за {stop - start}")
