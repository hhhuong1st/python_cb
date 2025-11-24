print("== Câu 4 ==")
i=1
dem = 0
while(i<=10):
    try:
        so = int(input(f"Nhập số thứ {i}: "))
        i += 1
        if (so<0):
            dem += 1
    except ValueError:
        print("Lỗi kiểu dữ liệu")
print (f"Có {dem} số âm")