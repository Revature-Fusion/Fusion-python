import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
        conn = psycopg2.connect(
            database='postgres',
            user='postgres',
            password='password',
            host='fusion-db.cfnl7bnhgahp.us-east-2.rds.amazonaws.com',
            port='5432'
        )

        return conn
    except OperationalError as e:
        print(f"{e}")
        return None


connection = create_connection()


def _test():
    print(connection)

