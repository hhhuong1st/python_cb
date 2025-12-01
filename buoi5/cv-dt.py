try:
    cd = float(input("Nhập chiều dài: "))
    cr= float(input("Nhập chiều rộng: "))
except ValueError:
    print ("Lỗi kiểu dữ liệu")
else:
    def cvhcn (cd,cr):
        cv = (cd+cr)*2
        return cv
    def dthcn (cd,cr):
        dt = cd * cr
        return dt
    def cvdt (cd,cr):
        cv = (cd+cr)*2
        dt = cd * cr
        return dt,cv
    cvdthcn = cvdt(cd,cr) # 

    print (f"Chu vi, diện tích hình chữ nhật là: {cvdthcn}") 
    print (f"Chu vi hình chữ nhật là: {cvdthcn[0]} Diện tích hình chữ nhật là: {cvdthcn[1]}") 