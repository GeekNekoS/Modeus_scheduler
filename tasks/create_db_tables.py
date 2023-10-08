import psycopg2

try:
    connection = psycopg2.connect('postgresql://postgres:1@localhost:5432/schedules')
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE Customers (
            id INTEGER,
            name VARCHAR,
            surname VARCHAR,
            birthdate DATE,
            PRIMARY KEY (id)
        );
    """)

    connection.commit()

    cursor.close()
    connection.close()
    
except Exception as ex:
    print('Can`t establish connection to database')
    print(ex)

# доделать
