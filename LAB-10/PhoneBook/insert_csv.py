import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='PhoneBook',
    user='postgres',
    password='minehome'
    )
cur = conn.cursor()
conn.commit()
import csv
filename = 'phones.csv'
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        name,phone_number = row
        cur.execute(f"""INSERT INTO phone_numbers_data(name,phone_number) VALUES
                    ('{name}','{phone_number}');
        """)
        conn.commit()


