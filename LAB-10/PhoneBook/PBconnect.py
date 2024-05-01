import psycopg2
from PBconfig import load_config

def connect(PBconfig):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**PBconfig) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    PBconfig = load_config()
    connect(PBconfig)