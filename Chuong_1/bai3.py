class PS:
    def __init__(self, tuso=0, mauso=1):
        self.tuso = tuso
        self.mauso = mauso

    def nhap_phan_so(self):
        self.tuso = int(input("Nhập tử số: "))
        self.mauso = int(input("Nhập mẫu số (khác 0): "))

    def kiem_tra_hop_le(self):
        return self.mauso != 0

    def in_phan_so(self):
        print(f"Phân số là: {self.tuso}/{self.mauso}")


ps = PS()

# Nhập phân số
ps.nhap_phan_so()

# In phân số ra màn hình
ps.in_phan_so()

# Kiểm tra tính hợp lệ của phân số
if ps.kiem_tra_hop_le():
    print("Phân số hợp lệ.")
else:
    print("Phân số không hợp lệ.")