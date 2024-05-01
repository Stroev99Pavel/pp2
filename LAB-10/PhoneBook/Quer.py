import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='PhoneBook',
    user='postgres',
    password='minehome'
    )

cur = conn.cursor()

filter = input("What kind of filter you want to use? name or number?")
if filter == "name":
    n = input("Write name")
    cur.execute('SELECT name,phone_number FROM phone_numbers_data WHERE name = %s',(n,))
    print(cur.fetchall())
if filter == "number":
    n = input("Write number")
    cur.execute('SELECT name,phone_number FROM phone_numbers_data WHERE phone_number = %s',(n,))
    print(cur.fetchall())
