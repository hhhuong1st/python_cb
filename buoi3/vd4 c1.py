while True:
    try:
        N = int(input("Nhập N: "))
        if N > 0:
            i = 1
            while i <= N:
                print(i, end=" ")
                i += 1
            print() 
            break 
        else:
            print("N phải lớn hơn 0")
    except ValueError:
        print("Lỗi kiểu dữ liệu")
