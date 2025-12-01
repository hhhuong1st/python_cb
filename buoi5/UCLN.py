while True:
    import ham_UC_BC
    try:
        A = int(input("Nhập A: "))
        B = int(input("Nhập B: "))
        if A > 0 and B > 0:
            break
    except ValueError:
        print ("Lỗi kiểu dữ liệu")

print (f"Ước chung lớn nhất của A {A} và B {B} là: {ham_UC_BC.UCLN(A,B)}")