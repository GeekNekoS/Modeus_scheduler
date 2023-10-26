import psycopg2

try:
    with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE lessons (
                id SERIAL PRIMARY KEY,
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
            CREATE TABLE directions (
                id SERIAL PRIMARY KEY,
                direction VARCHAR,
                schedule_url VARCHAR,
                FOREIGN KEY (id) REFERENCES lessons(id) ON DELETE CASCADE
            );
        """)
except Exception as ex:
    print(f"Can`t establish connection to database: {ex}\n")
