import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='PhoneBook',
    user='postgres',
    password='minehome'
    )
cur = conn.cursor()
Name = input("Name = ")
Surname = input("Surname = ")
PhoneNumber = input("Number = ")
cur.execute("""INSERT INTO phone_numbers_data(name,surname,phone_number) VALUES(%s,%s,%s)""",(Name,Surname,PhoneNumber))
conn.commit()