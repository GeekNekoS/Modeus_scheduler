import psycopg2

try:
    with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE lessons (
                lesson VARCHAR,
                module_url VARCHAR
            );
        """)
except Exception as ex:
    print(f"Can`t establish connection to database: {ex}\n")

try:
    with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE itis (
                id INTEGER,
                itis_1 VARCHAR,
                itis_2 VARCHAR,
                itis_3 VARCHAR,
                PRIMARY KEY (id)
            );
        """)
except Exception as ex:
    print(f"Can`t establish connection to database: {ex}\n")
