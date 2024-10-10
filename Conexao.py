import sqlite3

def connect_to_database(database_name='mydatabase.db'):
    try:
        conn = sqlite3.connect(database_name)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
