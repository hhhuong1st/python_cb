import hcn
try:
    cd = float(input("Nhập chiều dài: "))
    cr= float(input("Nhập chiều rộng: "))
except ValueError:
    print ("Lỗi kiểu dữ liệu")
else:
    cvdthcn = hcn.cvdt(cd,cr) # tuple
    print (f"Chu vi, diện tích hình chữ nhật là: {cvdthcn}") 
    print (f"Chu vi hình chữ nhật là: {cvdthcn[0]} Diện tích hình chữ nhật là: {cvdthcn[1]}")