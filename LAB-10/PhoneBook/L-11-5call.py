import psycopg2
from PBconfig import load_config
def PUSH(name, surname ="", phone_number=""):
    params = load_config()
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL DELETE_USER(%s,%s,%s)', (name, surname, phone_number))
            conn.commit()
        print("Stored procedure executed successfully!")
    except psycopg2.Error as e:
        print(e)

try:
    PUSH('Alexei')
except Exception as e:
    print("Error:", e)

