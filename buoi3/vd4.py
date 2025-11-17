dk = True
while dk:
    try:
        N = int(input("Nhập N: "))
        
    except ValueError:
        print("Lỗi kiểu dữ liệu")
    else:
        if N>0:
            i = 1
            while i <= N:
                print(i, end=" ")
                i += 1
            print() 
            break
            