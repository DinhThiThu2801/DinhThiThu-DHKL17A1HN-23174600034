import sqlite3

def list_tables(database_file):
    conn = sqlite3.connect(database_file)

    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    if tables:
        print("Các bảng trong cơ sở dữ liệu:")
        for table in tables:
            print(table[0])
    else:
        print("Không có bảng nào trong cơ sở dữ liệu.")

    conn.close()

def insert_and_display_records(database_file, table_name):
    conn = sqlite3.connect(database_file)

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", ('John Doe', 25))
    cursor.execute(f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", ('Jane Doe', 30))

    conn.commit()

    cursor.execute(f"SELECT * FROM {table_name}")

    rows = cursor.fetchall()
    if rows:
        print(f"\nDữ liệu từ bảng {table_name}:")
        for row in rows:
            print(row)
    else:
        print(f"\nKhông có dữ liệu trong bảng {table_name}.")

    conn.close()

database_path = 'my_database.db'

table_name = 'students'

list_tables(database_path)

insert_and_display_records(database_path, table_name)
