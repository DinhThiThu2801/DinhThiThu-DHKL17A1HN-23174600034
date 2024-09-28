class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def chu_vi(self):
        return self.a + self.b + self.c
    
    def dien_tich(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, (a**2 + b**2)**0.5)

class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, b)

class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a)

tam_giac_vuong = TamGiacVuong(3, 4)
print("Chu vi tam giác vuông là:", tam_giac_vuong.chu_vi())
print("Diện tích tam giác vuông là:", tam_giac_vuong.dien_tich())

tam_giac_can = TamGiacCan(5, 5)
print("Chu vi tam giác cân là:", tam_giac_can.chu_vi())
print("Diện tích tam giác cân là:", tam_giac_can.dien_tich())

tam_giac_deu = TamGiacDeu(6)
print("Chu vi tam giác đều là:", tam_giac_deu.chu_vi())
print("Diện tích tam giác đều là:", tam_giac_deu.dien_tich())
