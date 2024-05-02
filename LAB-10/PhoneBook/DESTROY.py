import psycopg2
conn = psycopg2.connect(
    host='localhost',
    dbname='PhoneBook',
    user='postgres',
    password='minehome'
    )

cur = conn.cursor()

cur.execute('DROP TABLE phone_numbers_data;')
conn.commit()