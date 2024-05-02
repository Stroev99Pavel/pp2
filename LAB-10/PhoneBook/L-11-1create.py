import psycopg2
from PBconfig import load_config
def create_func():
    commands = (
        """
        CREATE OR REPLACE FUNCTION FindBy(
            p_pattern varchar
        )
        RETURNS TABLE (
            name varchar,
            surname varchar,
            phone_number varchar
        )AS $$
        BEGIN
            RETURN QUERY
            SELECT name, surname, phone_number
            FROM phone_numbers_data
            WHERE name LIKE '%' || p_pattern || '%'
                OR surname LIKE '%' || p_pattern || '%'
                OR phone_number LIKE '%' || p_pattern || '%';
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
    create_func()