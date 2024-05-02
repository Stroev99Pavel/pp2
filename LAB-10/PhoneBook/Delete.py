import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='PhoneBook',
    user='postgres',
    password='minehome'
    )

cur = conn.cursor()
how = input("By what do you want to delete? name or number or surname? ")
if how == "surname":
    n = input("Write surname ")
    cur.execute("""DELETE FROM phone_numbers_data
                WHERE surname = %s;
    """,(n,))
    conn.commit()
if how == "name":
    n = input("Write name ")
    cur.execute("""DELETE FROM phone_numbers_data
                WHERE name = %s;
    """,(n,))
    conn.commit()
if how == "number":
    n = input("Write number ")
    cur.execute("""DELETE FROM phone_numbers_data
                WHERE phone_number = %s;
    """,(n,))
    conn.commit()