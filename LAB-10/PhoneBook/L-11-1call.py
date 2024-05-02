import psycopg2
from PBconfig import load_config


def get_parts(pattern):
    params = load_config()
    parts = []
    try:
        with  psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.callproc('FindBy', (pattern,))
                rows = cur.fetchall()
                for row in rows:
                    parts.append(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return parts


if __name__ == '__main__':
    pattern = input("Write a pattern ")
    parts = get_parts(pattern)
    print(parts)
