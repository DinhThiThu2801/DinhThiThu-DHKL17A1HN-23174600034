import xml.dom.minidom
#Sử dụng hàm parse() để đọc và phân tích file "sample.xml sau đó chuyển đổi nó thành biến đối tượng 'doc'.
doc = xml.dom.minidom.parse("sample.xml")

#Lấy danh sách các phần tử <staff>
staffs = doc.getElementsByTagName("staff")

#Duyệt qua từng phần tử <staff> và in ra thông tin
for staff in staffs:
#Lấy thông tin của mỗi nhân viên
    name = staff.getElementsByTagName("name")[0].firstChild.data
    salary = staff.getElementsByTagName("salary")[0].firstChild.data
    
#In ra thông tin của nhân viên
    print(f"Name: {name}")
    print(f"Salary: {salary}")