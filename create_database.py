import sqlite3
import contextlib
from pathlib import Path


def create_connection(db_file: str):
    """ Create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def create_users_table(db_file: str) -> None:
    """ Create a table for users with a login_time column """
    query = '''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            email TEXT
        );
    ''' 

    with contextlib.closing(create_connection(db_file)) as conn:
        if conn:
            with conn:
                conn.execute(query)


def create_logins_table(db_file: str) -> None:
    """ Create a separate table for storing login history """
    query = '''
        CREATE TABLE IF NOT EXISTS logins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            login_time TEXT NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        );
    '''

    with contextlib.closing(create_connection(db_file)) as conn:
        if conn:
            with conn:
                conn.execute(query)


def add_login_time_column(db_file: str) -> None:
    """ Add login_time column to users table if it doesn't exist (legacy support) """
    with contextlib.closing(create_connection(db_file)) as conn:
        if conn:
            cursor = conn.cursor()
            # Check if the column exists
            cursor.execute("PRAGMA table_info(users);")
            columns = [column[1] for column in cursor.fetchall()]

            if "login_time" not in columns:
                cursor.execute("ALTER TABLE users ADD COLUMN login_time TEXT;")
                conn.commit()
                print("Column 'login_time' added to the 'users' table.")


def setup_database(name: str) -> None:
    """ Set up the database by creating necessary tables """
    if not Path(name).exists():
        print(f"\033[91mCreating new database '{name}'\033[0m")
        create_connection(name)

    create_users_table(name)
    create_logins_table(name)  # Ensure the login history table exists
    add_login_time_column(name)  # Ensure old table is updated


# Example usage:
database = "users.db"
setup_database(database)
