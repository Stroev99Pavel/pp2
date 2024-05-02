import psycopg2
from PBconfig import load_config


def get_parts(pattern):
    params = load_config()
    parts = []
    try:
        with  psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur = conn.cursor()
                cur.callproc('FindBy', (pattern,))
                row = cur.fetchone()
                while row is not None:
                    parts.append(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return parts


if __name__ == '__main__':
    pattern = input("Write a pattern ")
    parts = get_parts(pattern)
    print(parts)