import xml.dom.minidom
def main():
    #Sử dụng hàm parse() để đọc và phân tích file "sample.xml sau đó chuyển đổi nó thành biến đối tượng 'doc'.
    doc=xml.dom.minidom.parse("E:\DinhThiThu-DHKL17A1HN-23174600034\Chuong_2\sample.xml");

    #In ra In ra tên của node gốc và tag name của node đầu tiên trong file .xml
    print(doc.nodeName)
    print(doc.firstChild.tagName)
if __name__=="__main__":
    main();