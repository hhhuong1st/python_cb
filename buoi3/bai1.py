try:
    Van = float(input("Nhập điểm môn Văn: "))
    Toan = float(input("Nhập điểm môn Toán: "))
    Anh = float(input("Nhập điểm môn Anh: "))
except ValueError:
    print ("Lỗi kiểu dữ liệu")
else:
    dtb = (Van + Toan + Anh) /3
    if Van < 0 or Van > 10 or Toan < 0 or Toan > 10 or Anh < 0 or Anh > 10:
        print ("Lỗi nhập sai giá trị")
    else:
        if (dtb >= 9):
            print ("Xếp loại xuất sắc")
        elif (dtb >=8):
            print ("Xếp loại giỏi")
        elif (dtb >=7):
            print ("Xếp loại khá")
        elif (dtb >=5):
            print ("Xếp loại trung bình")
        else:
            print ("Xếp loại yếu")