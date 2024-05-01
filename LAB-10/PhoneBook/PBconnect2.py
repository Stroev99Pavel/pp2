import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='PhoneBook',
    user='postgres',
    password='minehome'
    )

cur = conn.cursor()
#connection to database
cur.execute('SELECT Version()')
db_ver=cur.fetchall()
print(db_ver)