from parsing.schedules.create_and_fill_lessons_table import create_and_fill_lessons_table
from parsing.schedules.create_and_fill_directions_table import create_and_fill_directions_table
from parsing.schedules.create_and_fill_schedules_table import create_and_fill_schedules_table

import time


def main(user_id):
    start = time.perf_counter()

    create_and_fill_lessons_table(user_id)
    create_and_fill_directions_table(user_id)
    create_and_fill_schedules_table(user_id)

    stop = time.perf_counter()

    print(f"Выполнено за {stop - start}")


if __name__ == "__main__":
    main(user_id)
