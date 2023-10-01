import psycopg2

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='test', user='postgres', password='secret', host='host')
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')
