import sqlite3

conn = sqlite3.connect('ql_nhan_vien.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS PHONG (
        Id INTEGER PRIMARY KEY NOT NULL,
        Name TEXT NOT NULL,
        quanly TEXT NOT NULL,
        so_luong_nhan_vien INTEGER NOT NULL
    )
''')

cursor.executemany('''
    INSERT INTO PHONG (Name, quanly, so_luong_nhan_vien)
    VALUES (?, ?, ?)
''', [
    ('Phòng A', 'Người quản lý A', 10),
    ('Phòng B', 'Người quản lý B', 8),
])
cursor.execute('''
    CREATE TABLE IF NOT EXISTS NHAN_VIEN (
        id INTEGER PRIMARY KEY NOT NULL,
        ho_ten TEXT NOT NULL,
        tuoi INTEGER NOT NULL,
        dia_chi TEXT NOT NULL,
        luong REAL NOT NULL,
        Id_phong INTEGER,
        FOREIGN KEY (Id_phong) REFERENCES PHONG(Id)
    )
''')
conn.commit()
conn.close()
