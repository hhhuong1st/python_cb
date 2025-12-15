try:
    Tuoi = [12,15,14,18,16,13,20,17,11]
except ValueError:
    print ("Lỗi kiểu dữ liệu")
else:
    # a
    tong = 0
    for value in Tuoi:
        tong += value
        tb = tong / len(Tuoi)
    print (f"Tuổi trung bình là: {tb}")
    # b
    min = Tuoi[0]
    for value in Tuoi:
        if value < min:
            min = value
    print (f"Tuổi nhỏ nhất là: {min}")
    # c
    lon = 0
    nho = 0
    for value in Tuoi:
        if value >= 16:
            lon += 1
        else:
            nho += 1
    print (f"Đếm số người >= 16 là: {lon}")
    print (f"Đếm số người < 16 là: {nho}")
    # d
    for i in range (len(Tuoi)):
        for j in range (i + 1, len(Tuoi)):
            if Tuoi[i] < Tuoi [j]:
                Tuoi[i], Tuoi[j] = Tuoi[j], Tuoi[i]
    print (f"Sắp xếp giảm dần và in ra (1,0): {Tuoi}")