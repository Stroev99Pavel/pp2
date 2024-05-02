import psycopg2
from PBconfig import load_config
def create_proc():
    commands = (
        """
        CREATE OR REPLACE PROCEDURE add_or_change(
            p_name varchar,
            p_surname varchar,
            p_phone_number varchar
        )
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM phone_numbers_data WHERE name = p_name AND surname = p_surname) THEN
                UPDATE phone_numbers_data
                SET phone_number = p_phone_number
                WHERE name = p_name AND surname = p_surname;
            ELSE
                INSERT INTO phone_numbers_data (name, surname, phone_number)
                VALUES (p_name, p_surname, p_phone_number);
            END IF;
        END;
        $$
        LANGUAGE PLPGSQL;
        """,
    )
    try:
        PBconfig = load_config()
        with psycopg2.connect(**PBconfig) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    create_proc()