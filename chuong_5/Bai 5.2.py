import sqlite3
conn = sqlite3.connect(':memory:')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT
    )
''')

cursor.execute("INSERT INTO employees (name, position) VALUES (?, ?)", ('John Doe', 'Developer'))
cursor.execute("INSERT INTO employees (name, position) VALUES (?, ?)", ('Jane Doe', 'Designer'))

conn.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

print("Dữ liệu trong bảng employees:")
for row in rows:
    print(row)
conn.close()
