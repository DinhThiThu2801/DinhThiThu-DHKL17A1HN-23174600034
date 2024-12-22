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

database_path = 'my_database.db'
list_tables(database_path)
