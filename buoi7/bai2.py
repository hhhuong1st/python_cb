def nhap_so_duong():
    while True:
        try:
            x = float(input("Nhập số km (>0): "))
            if x > 0:
                return x
            print("Số km phải > 0. Nhập lại.")
        except ValueError:
            print("Dữ liệu không hợp lệ. Nhập lại.")

def tinh_cuoc_taxi(x):
    tien = 0

    if x <= 1:
        tien = 15000
    elif x <= 10:
        tien = 15000 + (x - 1) * 13500
    else:
        tien = 15000 + 9 * 13500 + (x - 10) * 11000

    # Giảm giá nếu trên 20 km
    if x > 20:
        tien = tien * 0.95

    return tien

# Chạy chương trình
km = nhap_so_duong()
cuoc = tinh_cuoc_taxi(km)
print(f"Số tiền phải trả: {cuoc:,.0f} đ")

import random

def nap_nang_luong():
    nang_luong = 0

    for lan in range(1, 6):
        print(f"Lần nạp {lan}")

        if random.random() < 0.5:
            tang = random.randint(15, 40)
            nang_luong += tang
            print(f"Nạp thành công, +{tang} năng lượng")
        else:
            giam = random.randint(5, 15)
            nang_luong -= giam
            if nang_luong < 0:
                nang_luong = 0
            print(f"Nạp thất bại, -{giam} năng lượng")

        print(f"Năng lượng hiện tại: {nang_luong}")

        if nang_luong >= 120:
            print("🎉 THÀNH CÔNG (đạt >= 120 năng lượng)")
            return nang_luong

    print("THẤT BẠI (sau 5 lần vẫn < 120)")
    return nang_luong

# Chạy trò chơi
ketqua = nap_nang_luong()
print("Năng lượng cuối:", ketqua)

Tuoi = [12, 15, 14, 18, 16, 13, 20, 17, 11]
def tuoi_trung_binh(Tuoi):
    tong = 0
    dem = 0
    for t in Tuoi:
        tong += t
        dem += 1
    return tong / dem
def tuoi_nho_nhat(Tuoi):
    min_tuoi = Tuoi[0]
    for t in Tuoi:
        if t < min_tuoi:
            min_tuoi = t
    return min_tuoi
def dem_do_tuoi(Tuoi):
    du_16 = 0
    duoi_16 = 0

    for t in Tuoi:
        if t >= 16:
            du_16 += 1
        else:
            duoi_16 += 1

    return du_16, duoi_16
