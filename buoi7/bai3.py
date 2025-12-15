try:
    Diem = [7.5,8.0,6.0,9.0,5.5,8.5,7.0,6.5]
except ValueError:
    print ("Lỗi kiểu dữ liệu")
else:
    # a
    tong = 0
    for value in Diem:
        tong += value
        tb = tong / len(Diem)
    print (f"Điểm trung bình là: {tb}")
    # b
    max = Diem[0]
    for value in Diem:
        if value > max:
            max = value
    print (f"Điểm cao nhất là: {max}")
    # c
    lon = 0
    nho = 0
    for value in Diem:
        if value >= 8:
            lon += 1
        else:
            nho += 1
    print (f"Đếm số điểm >= 8.0 là: {lon}")
    print (f"Đếm số điểm < 8.0 là: {nho}")