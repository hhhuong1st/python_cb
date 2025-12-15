NhietDo = [30,28,35,33,29,31,27,34]
tong = 0
for value in NhietDo:
    tong += value
    tb = tong / len(NhietDo)
print (f"Nhiệt độ trung bình là: {tb}")
# b
max = NhietDo[0]
for value in NhietDo:
    if value > max:
        max = value
print (f"Nhiệt độ cao nhất là: {max}")
# c
lon = 0
nho = 0
for value in NhietDo:
    if value >= 32:
        lon += 1
    else:
        nho += 1
print (f"Đếm số ngày nóng >= 32 là: {lon}")
print (f"Đếm số ngày không nóng < 32 là: {nho}")