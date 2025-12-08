def NhapN():
        try:
            n = str(print ("Nhập chuỗi: "))
        except ValueError:
            print("Lỗi kiểu dữ liệu")

def cau1(N):
    print("Chiều dài chuỗi là:", len(N))

# print ("===Câu 1===")
# s = str(input("Nhập: "))
# print ("Chiều dài chuỗi là: ",len(s))

# print ("===Câu 3===")
# kitudau = s[:3]
# kitucuoi = s[3:]
# print (f"3 kí tự đầu tiên là: {kitudau}")
# print (f"3 kí tự cuối là: {kitucuoi}")

# print ("===Câu 4===")
# print(f"In ra dạng viết hoa là: {s.upper()}")
# print(f"In ra dạng viết thường là: {s.lower()}")


# print ("===Câu 5===")
# ho = str(input("Nhập họ: "))
# tendem = str(input("Nhập tên đệm: "))
# ten = str(input("Nhập tên: "))
# hovaten = "Họ và tên là: {}" 
# print(hovaten.format(ho),(tendem), (ten)) 

# print ("===Câu 6===")
# cau6 = str(input("Nhập vào một câu: "))
# kt = str(input("kiểm tra có xuất hiện không: "))
# kiemtra=cau6.startswith(kt,0,15)
# print (kiemtra)

# print ("===Câu 7===")
# cau7 = "2023/10/25"
# print (cau7.replace("/","-"))


# print ("===Câu 8===")
# b = "           huong           " 
# a = b.strip(" ") 
# print(a)

# print ("===Câu 9===")
