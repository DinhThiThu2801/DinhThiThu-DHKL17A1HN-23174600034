import sqlite3

def count_records(database_file, table_name):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"Số bản ghi trong bảng {table_name}: {count}")

    conn.close()

database_path = 'my_database.db'
table_name = 'students'
count_records(database_path, table_name)
