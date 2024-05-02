import psycopg2
from PBconfig import load_config
def create_proc():
    commands = (
        """
        CREATE OR REPLACE PROCEDURE DELETE_USER(
            p_name varchar,
            p_surname varchar,
            p_phone_number varchar
        )
        AS $$
        BEGIN
            DELETE FROM phone_numbers_data
            WHERE name = p_name OR surname = p_surname;
            DELETE FROM phone_numbers_data
            WHERE phone_number = p_phone_number;
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