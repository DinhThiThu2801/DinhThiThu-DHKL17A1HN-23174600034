import sqlite3

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')
conn.commit()
conn.close()
