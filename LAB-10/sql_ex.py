#Create - INSERT
#Read - Select
#Update - UPDATE
#Delete - Delete
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

#Create new students
cur.execute("""INSERT INTO students_data(name,id,study_year,phone_number) VALUES
            ('Pavel', '24B031901', 1, '+77472460872'),
            ('Viktor', '24B031902', 1, '+77473460871');
""")
conn.commit()

#Get students
cur.execute('SELECT name, id, phone_number, study_year FROM students_data')
print (cur.fetchall())

cur.execute('SELECT name, id, phone_number, study_year FROM students_data')
print (cur.fetchone())
print (cur.fetchone())
print (cur.fetchone())

#Update student
cur.execute("""UPDATE students_data
            SET study_year = 2
            WHERE name = 'Pavel';
""")
conn.commit()

#Update every student
cur.execute("""UPDATE students_data
            SET study_year = 2;
""")
conn.commit()

#Update student by ID
cur.execute("""UPDATE students_data
            SET study_year = 2
            WHERE id = '24B031901';
""")
conn.commit()

#Delete students
cur.execute("""DELETE FROM students_data
            WHERE id = '24B031901';
""")
conn.commit()
