from tasks.create_db_tables import create_db_tables
from work_with_db.create_lessons_table import main as create_lessons_table
from work_with_db.create_directions_table import main as create_directions_table


if __name__ == "__main__":
    create_db_tables()
    create_lessons_table()
    create_directions_table()
