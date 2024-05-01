import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='PhoneBook',
    user='postgres',
    password='minehome'
    )
cur = conn.cursor()
Name = input("Name = ")
PhoneNumber = input("Number = ")
cur.execute("""INSERT INTO phone_numbers_data(name,phone_number) VALUES(%s,%s)""",(Name,PhoneNumber))
conn.commit()