class Date:
    def __init__(self, ngay=1, thang=1, nam=1900):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self):
        print(f"Ngày: {self.ngay}/{self.thang}/{self.nam}")

    def next(self):
        import datetime
        current_date = datetime.date(self.nam, self.thang, self.ngay)
        next_date = current_date + datetime.timedelta(days=1)
        self.ngay = next_date.day
        self.thang = next_date.month
        self.nam = next_date.year

# Tạo 1 data ngày
ngay = Date(26, 9, 2023)

# In thông tin về ngày
ngay.display()

# Tính ngày tiếp theo và in kết quả
ngay.next()
ngay.display()