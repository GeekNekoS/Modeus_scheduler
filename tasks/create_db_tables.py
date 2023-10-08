import psycopg2

try:
    conn = psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE Customers (
            id INTEGER,
            name VARCHAR,
            surname VARCHAR,
            birthdate DATE,
            PRIMARY KEY (id)
        );
    """)

    all_users = cursor.fetchall()
    cursor.close()
    conn.close()
except Exception as ex:
    print('Can`t establish connection to database')
    print(ex)

# доделать
