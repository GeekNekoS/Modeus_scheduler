from work_with_db_draft.create_db_tables import create_db_tables
from work_with_db_draft.fill_lessons_table import main as fill_lessons_table
from work_with_db_draft.fill_directions_table import main as fill_directions_table
from work_with_db_draft.fill_schedules_tables import main as fill_schedules_tables


if __name__ == "__main__":
    create_db_tables()
    fill_lessons_table()
    fill_directions_table()
    fill_schedules_tables()
