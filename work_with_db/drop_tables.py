import psycopg2
import os

from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')


def drop_table(name):
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            query = f"DROP TABLE {name};"
            cursor.execute(query)
            print(f"Таблица {name} успешно удалена")
    except Exception as ex:
        print(f"Can`t establish connection to database: {ex}\n")


def main():
    table_name = input("Введите название таблицы, которую хотите удалить: ")
    drop_table(table_name)


if __name__ == "__main__":
    main()
