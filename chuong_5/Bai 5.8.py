import sqlite3

def xoa_hang(database_file, ten_bang, dieu_kien):
    conn = sqlite3.connect(database_file)

    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM {ten_bang} WHERE {dieu_kien}")
    conn.commit()

    print(f"Xóa hàng thành công từ bảng {ten_bang} dựa trên điều kiện: {dieu_kien}")
    conn.close()
duong_dan_csdls = 'nhan_su.db'
ten_bang_can_xoa_hang = 'nhan_vien'
dieu_kien_xoa = 'ID = 1'
xoa_hang(duong_dan_csdls, ten_bang_can_xoa_hang, dieu_kien_xoa)
