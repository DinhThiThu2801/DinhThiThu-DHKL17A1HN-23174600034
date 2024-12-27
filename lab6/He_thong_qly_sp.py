import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite (hoặc tạo mới nếu chưa có)
conn = sqlite3.connect('sanpham.db')
cursor = conn.cursor()

# Tạo bảng sản phẩm nếu chưa tồn tại
cursor.execute('''CREATE TABLE IF NOT EXISTS sanpham (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ten TEXT NOT NULL,
                    gia REAL NOT NULL)''')
conn.commit()

# Hàm thêm sản phẩm
def them_san_pham():
    ten = nhap_ten.get()
    gia = nhap_gia.get()
    if ten and gia:
        cursor.execute("INSERT INTO sanpham (ten, gia) VALUES (?, ?)", (ten, float(gia)))
        conn.commit()
        cap_nhat_danh_sach()
        nhap_ten.delete(0, tk.END)
        nhap_gia.delete(0, tk.END)
    else:
        messagebox.showwarning("Lỗi Nhập", "Vui lòng điền đầy đủ thông tin")

# Hàm cập nhật danh sách sản phẩm
def cap_nhat_danh_sach():
    danh_sach.delete(0, tk.END)
    cursor.execute("SELECT * FROM sanpham")
    rows = cursor.fetchall()
    for row in rows:
        danh_sach.insert(tk.END, f"{row[1]} - ${row[2]:.2f}")

# Hàm tìm kiếm sản phẩm
def tim_kiem_san_pham():
    ten = nhap_tim_kiem.get()
    if ten:
        cursor.execute("SELECT * FROM sanpham WHERE ten LIKE ?", ('%' + ten + '%',))
        rows = cursor.fetchall()
        danh_sach.delete(0, tk.END)
        for row in rows:
            danh_sach.insert(tk.END, f"{row[1]} - ${row[2]:.2f}")
    else:
        cap_nhat_danh_sach()

# Hàm xóa sản phẩm
def xoa_san_pham():
    try:
        selected = danh_sach.curselection()
        if selected:
            ten_san_pham = danh_sach.get(selected[0]).split(" - ")[0]
            cursor.execute("DELETE FROM sanpham WHERE ten = ?", (ten_san_pham,))
            conn.commit()
            cap_nhat_danh_sach()
        else:
            messagebox.showwarning("Lỗi Chọn", "Vui lòng chọn sản phẩm để xóa")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi: {str(e)}")

# Tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Hệ Thống Quản Lý Sản Phẩm")

# Tạo các widget
label_ten = tk.Label(cua_so, text="Tên Sản Phẩm:")
label_ten.grid(row=0, column=0)

nhap_ten = tk.Entry(cua_so)
nhap_ten.grid(row=0, column=1)

label_gia = tk.Label(cua_so, text="Giá Sản Phẩm:")
label_gia.grid(row=1, column=0)

nhap_gia = tk.Entry(cua_so)
nhap_gia.grid(row=1, column=1)

nut_them = tk.Button(cua_so, text="Thêm Sản Phẩm", command=them_san_pham)
nut_them.grid(row=2, column=0, columnspan=2)

label_tim_kiem = tk.Label(cua_so, text="Tìm Kiếm Sản Phẩm:")
label_tim_kiem.grid(row=3, column=0)

nhap_tim_kiem = tk.Entry(cua_so)
nhap_tim_kiem.grid(row=3, column=1)

nut_tim_kiem = tk.Button(cua_so, text="Tìm Kiếm", command=tim_kiem_san_pham)
nut_tim_kiem.grid(row=4, column=0, columnspan=2)

nut_xoa = tk.Button(cua_so, text="Xóa Sản Phẩm", command=xoa_san_pham)
nut_xoa.grid(row=5, column=0, columnspan=2)

# Listbox để hiển thị danh sách sản phẩm
danh_sach = tk.Listbox(cua_so, width=50, height=10)
danh_sach.grid(row=6, column=0, columnspan=2)

# Cập nhật danh sách sản phẩm khi khởi động
cap_nhat_danh_sach()

# Chạy ứng dụng
cua_so.mainloop()

# Đóng kết nối cơ sở dữ liệu khi thoát ứng dụng
conn.close()
