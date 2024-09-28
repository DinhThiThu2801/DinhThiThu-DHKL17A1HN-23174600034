class Hinh_Chu_Nhat:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def dien_tich_hcn(self):
        return self.length * self.width

    def chu_vi_hcn(self):
        return 2 * (self.length + self.width)

Hinh_Chu_Nhat = Hinh_Chu_Nhat(8, 4) 
dientich = Hinh_Chu_Nhat.dien_tich_hcn()  
chuvi = Hinh_Chu_Nhat.chu_vi_hcn() 

print("Độ dài 2 cạnh của hình chữ nhật lần lượt là: ", Hinh_Chu_Nhat.length, Hinh_Chu_Nhat.width)
print("Diện tích của hình chữ nhật là:", dientich)
print("Chu vi của hình chữ nhật là:", chuvi)        