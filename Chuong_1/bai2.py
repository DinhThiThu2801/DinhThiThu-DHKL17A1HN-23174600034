class TS:
    def __init__(self, hoten='', diem_toan=0, diem_ly=0, diem_hoa=0):
        self.hoten = hoten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap_thong_tin(self):
        self.hoten = input("Nhập họ và tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def in_thong_tin(self):
        print("Họ và tên:", self.hoten)
        print("Điểm Toán:", self.diem_toan)
        print("Điểm Lý:", self.diem_ly)
        print("Điểm Hóa:", self.diem_hoa)

    def tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

# Nhập danh sách thí sinh
n = int(input("Nhập số lượng thí sinh: "))
ds_ts = [TS() for _ in range(n)]
for ts in ds_ts:
    ts.nhap_thong_tin()
    tong_diem = ts.tong_diem() 
print("Tổng điểm của thí sinh:", tong_diem)

# Sắp xếp danh sách thí sinh theo tổng điểm từ cao xuống thấp
ds_ts_trung_tuyen = sorted(ds_ts, key=lambda x: x.tong_diem(), reverse=True)

# In danh sách thí sinh trúng tuyển
print("Danh sách thí sinh trúng tuyển gồm:")
for ts in ds_ts_trung_tuyen:
    if ts.tong_diem() >= 20:
        ts.in_thong_tin()