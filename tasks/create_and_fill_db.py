from schedules_parsing.tasks.create_and_fill_lessons_table import create_and_fill_lessons_table
from schedules_parsing.tasks.create_and_fill_directions_table import create_and_fill_directions_table
from schedules_parsing.tasks.create_and_fill_schedules_table import create_and_fill_schedules_table

import time


if __name__ == "__main__":
    start = time.perf_counter()

    create_and_fill_lessons_table()
    create_and_fill_directions_table()
    create_and_fill_schedules_table()

    stop = time.perf_counter()

    print(f"Выполнено за {stop - start}")
