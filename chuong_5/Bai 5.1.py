import sqlite3

def create_database():
    connection = sqlite3.connect("mydatabase.db")

    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS example_table
                      (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

    connection.close()

def connect_and_print_version():
    connection = sqlite3.connect("mydatabase.db")
    cursor = connection.cursor()
    cursor.execute("SELECT SQLITE_VERSION()")
    version = cursor.fetchone()[0]
    print(f"SQLite version: {version}")
    connection.close()

create_database()

connect_and_print_version()
