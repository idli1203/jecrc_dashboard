import psycopg2

# PostgreSQL Connection Config
DB_CONFIG = {
    "host": "localhost",
    "database": "jecrc",
    "user": "admin",
    "password": "admin",
    "port": "5432",
}

# Function to Get a New Connection
def get_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print("Error connecting to database:", e)
        return None

# Function to Close Connection
def close_connection(conn):
    if conn:
        conn.close()
