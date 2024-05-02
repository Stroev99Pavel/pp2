import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='PhoneBook',
    user='postgres',
    password='minehome'
    )

cur = conn.cursor()

def FindByName(pattern):
    cur.execute("""
        SELECT *
        FROM phone_numbers_data
        WHERE name LIKE %s
        """, (f"%{pattern}%",))
    rows = cur.fetchall()
    for row in rows:
        print(row)
def FindBySurname(pattern):
    cur.execute("""
        SELECT *
        FROM phone_numbers_data
        WHERE surname LIKE %s
        """, (f"%{pattern}%",))
    rows = cur.fetchall()
    for row in rows:
        print(row)
def FindByNumber(pattern):
    cur.execute("""
        SELECT *
        FROM phone_numbers_data
        WHERE phone_number LIKE %s
        """, (f"%{pattern}%",))
    rows = cur.fetchall()
    for row in rows:
        print(row)
how = input("By what part do you whant to search? name,surname or number? ")
if how == "name":
    pattern = input("Enter a pattern (part of name)")
    print(FindByName(pattern))
if how == "surname":
    pattern = input("Enter a pattern (part of surname)")
    print(FindBySurname(pattern))
if how == "number":
    pattern = input("Enter a pattern (part of number)")
    print(FindByNumber(pattern))

