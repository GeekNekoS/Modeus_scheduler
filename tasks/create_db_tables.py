import psycopg2


try:
    with psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE Modules (
                id INTEGER,
                itis VARCHAR,
                history VARCHAR,
                math VARCHAR,
                ORG VARCHAR,
                physics VARCHAR,
                english VARCHAR,
                PRIMARY KEY (id)
            );
        """)
except Exception as ex:
    print(f"Can`t establish connection to database: {ex}\n")
