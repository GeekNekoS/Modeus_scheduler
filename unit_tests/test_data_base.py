import unittest
import psycopg2
import os

from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL_LOCAL')  # DATABASE_URL


class TestDataBase(unittest.TestCase):
    def test_directions_table_filling(self):
        lessons_info = None
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()
                query = """SELECT * FROM lessons"""
                cursor.execute(query)
                lessons_info = cursor.fetchall()
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

        existing_lessons = set()
        for lesson in lessons_info:
            lesson_id = lesson[0]
            existing_lessons.add(lesson_id)

        directions_info = None
        try:
            with psycopg2.connect(DATABASE_URL) as connection:
                cursor = connection.cursor()
                query = """SELECT * FROM directions"""
                cursor.execute(query)
                directions_info = cursor.fetchall()
        except Exception as ex:
            print(f"Can`t establish connection to database: {ex}\n")

        lessons_in_db = set()
        for direction in directions_info:
            direction_id = direction[3]
            lessons_in_db.add(direction_id)

        self.assertEqual(existing_lessons, lessons_in_db)


if __name__ == "__main__":
    unittest.main()
