
import math

def nhap_so_duong():
    while True:
        try:
            h = float(input("Nhập số giờ gửi (>0): "))
            if h > 0:
                return h
            print("Số giờ phải > 0. Nhập lại.")
        except ValueError:
            print("Dữ liệu không hợp lệ. Nhập lại.")

def tinh_tien_gui_xe(h):
    # Làm tròn giờ lên
    gio = math.ceil(h)

    tien = 0

    if gio <= 2:
        tien = gio * 5000
    elif gio <= 6:
        tien = 2 * 5000 + (gio - 2) * 4000
    else:
        tien = 2 * 5000 + 4 * 4000 + (gio - 6) * 3000

    return tien

# Chạy chương trình
h = nhap_so_duong()
tong_tien = tinh_tien_gui_xe(h)
print(f"Tổng tiền gửi xe: {tong_tien:,.0f} đ")


import random

def ban_muc_tieu():
    diem = 0

    for phat in range(1, 8):
        print(f"Phát bắn {phat}")

        if random.random() < 0.4:
            cong = random.randint(10, 25)
            diem += cong
            print(f"Trúng mục tiêu! +{cong} điểm")
        else:
            print("Trượt mục tiêu! +0 điểm")

        print(f"Tổng điểm hiện tại: {diem}")

        if diem >= 90:
            print("THẮNG (đạt >= 90 điểm)")
            return diem

    print("THUA (hết 7 phát mà chưa đạt 90 điểm)")
    return diem

# Chạy trò chơi
tong_diem = ban_muc_tieu()
print("Tổng điểm cuối:", tong_diem)


















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