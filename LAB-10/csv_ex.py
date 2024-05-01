#CSV - Comma Separated Values
#
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='students',
    user='postgres',
    password='minehome'
    )

cur = conn.cursor()
#connection to database

#Delete table
cur.execute('DROP TABLE students_data;')
conn.commit()

#Create table
cur.execute("""CREATE TABLE students_data(
            name VARCHAR(255),
            id VARCHAR(255) PRIMARY KEY,
            study_year INT,
            phone_number VARCHAR(20)
);
""")
conn.commit()
import csv
filename = 'students.csv'
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        name,id,study_year,phone_number = row

        #Create new students
        cur.execute(f"""INSERT INTO students_data(name,id,study_year,phone_number) VALUES
                    ('{name}', '{id}',{study_year}, '{phone_number}');
        """)
        conn.commit()


