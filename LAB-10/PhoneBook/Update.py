import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='PhoneBook',
    user='postgres',
    password='minehome'
    )

cur = conn.cursor()
who = input("Who do you want to change?")
change = input("What do you want change? name or phone?")
if change == "name":
    new = input("new name")
    cur.execute("""UPDATE phone_numbers_data 
                SET name = %s
                WHERE name = %s
    """,(new,who))
    conn.commit()
if change == "phone":
    new = input("new phone")
    cur.execute("""UPDATE phone_numbers_data 
                SET phone_number = %s
                WHERE name = %s
    """,(new,who))
    conn.commit()