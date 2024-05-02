import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='PhoneBook',
    user='postgres',
    password='minehome'
    )

cur = conn.cursor()

cur.execute("""CREATE TABLE phone_numbers_data(
            name VARCHAR(255),
            surname VARCHAR(255),
            phone_number VARCHAR(20)
);
""")
conn.commit()

#SELECT * FROM phone_numbers_data