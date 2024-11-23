import psycopg2

db_config = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'hw03',
    'user': 'postgres',
    'password': '567234'
}

def db_connect():
    """
    Establishes a connection to the PostgreSQL database using the provided configuration.

    :return: Connection object if successful, None otherwise
    """
    try:
        conn = psycopg2.connect(
            host=db_config['host'],
            port=db_config['port'],
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password']
        )

        print("Connected to the database.")

        return conn

    except Exception as error:
        print(f"Error while connecting to the database: {error}")
        if conn:
            conn.close()
            print("Database connection closed.")
