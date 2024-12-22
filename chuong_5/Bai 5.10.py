import sqlite3

conn = sqlite3.connect('product.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        Id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Price REAL NOT NULL,
        Amount INTEGER NOT NULL
    )
''')
conn.commit()

def display_products():
    cursor.execute('SELECT * FROM product')
    products = cursor.fetchall()
    if not products:
        print("Không có sản phẩm nào trong danh sách.")
    else:
        print("Danh sách sản phẩm:")
        print("Id\tName\tPrice\tAmount")
        for product in products:
            print(f"{product[0]}\t{product[1]}\t{product[2]}\t{product[3]}")

def add_product(name, price, amount):
    cursor.execute('INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)', (name, price, amount))
    conn.commit()
    print("Đã thêm sản phẩm thành công.")

def search_product_by_name(name):
    cursor.execute('SELECT * FROM product WHERE Name LIKE ?', (f'%{name}%',))
    products = cursor.fetchall()
    if not products:
        print(f"Không tìm thấy sản phẩm có tên chứa '{name}'.")
    else:
        print("Kết quả tìm kiếm:")
        print("Id\tName\tPrice\tAmount")
        for product in products:
            print(f"{product[0]}\t{product[1]}\t{product[2]}\t{product[3]}")

def update_product_price_quantity(product_id, new_price, new_quantity):
    cursor.execute('UPDATE product SET Price = ?, Amount = ? WHERE Id = ?', (new_price, new_quantity, product_id))
    conn.commit()
    print("Đã cập nhật thông tin sản phẩm thành công.")

def delete_product_by_id(product_id):
    cursor.execute('DELETE FROM product WHERE Id = ?', (product_id,))
    conn.commit()
    print("Đã xóa sản phẩm thành công.")
while True:
    print("\n1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Tìm kiếm sản phẩm theo tên")
    print("4. Cập nhật đơn giá và số lượng của một sản phẩm")
    print("5. Xóa một sản phẩm theo Id")
    print("0. Thoát")
    
    choice = input("Nhập lựa chọn của bạn: ")
    
    if choice == '1':
        display_products()
    elif choice == '2':
        name = input("Nhập tên sản phẩm: ")
        price = float(input("Nhập đơn giá sản phẩm: "))
        amount = int(input("Nhập số lượng sản phẩm: "))
        add_product(name, price, amount)
    elif choice == '3':
        search_name = input("Nhập tên sản phẩm cần tìm: ")
        search_product_by_name(search_name)
    elif choice == '4':
        product_id = int(input("Nhập Id sản phẩm cần cập nhật: "))
        new_price = float(input("Nhập đơn giá mới: "))
        new_quantity = int(input("Nhập số lượng mới: "))
        update_product_price_quantity(product_id, new_price, new_quantity)
    elif choice == '5':
        product_id = int(input("Nhập Id sản phẩm cần xóa: "))
        delete_product_by_id(product_id)
    elif choice == '0':
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
