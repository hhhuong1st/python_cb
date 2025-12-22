# def nhap_so_duong():
#     while True:
#         try:
#             x = float(input("Nhập x (m³) > 0: "))
#             if x > 0:
#                 return x
#             print("Giá trị phải > 0. Nhập lại.")
#         except ValueError:
#             print("Dữ liệu không hợp lệ. Nhập lại.")

# def tinh_tien_nuoc(x):
#     # Tiền nước trước phí môi trường
#     tien = 0.0

#     if x <= 10:
#         tien = x * 7000
#     elif x <= 20:
#         tien = 10 * 7000 + (x - 10) * 9000
#     else:
#         tien = 10 * 7000 + 10 * 9000 + (x - 20) * 12000

#     # Phí môi trường: 5% trên tiền nước (chưa gồm phí)
#     phimoitruong = tien * 0.05
#     tongtien = tien + phimoitruong
#     return tongtien

# # Chạy chương trình
# x = nhap_so_duong()

# tong = tinh_tien_nuoc(x)
# print(f"Tổng tiền phải trả (đã gồm phí môi trường): {tong:,.0f} đ")


import random

def san_kho_bau():
    diem = 0

    for i in range(1, 7):
        print("=> Lượt", i)

        if random.random() < 0.8:
            diemcong = random.randint(5, 30)
            diem += diemcong
            print(f"Tìm thấy kho báu, được cộng {diemcong} điểm")
        else:
            diem -= 2
            if diem < 0:
                diem = 0
            print("Không tìm thấy kho báu, bị trừ 2 điểm")

        print(f"Tổng điểm: {diem}")

        if diem >= 80:
            print("KẾT LUẬN: Thắng (đạt >= 80 điểm)")
            return diem

    # Sau 6 lượt
    if diem < 80:
        print("KẾT LUẬN: Thua (hết 6 lượt mà chưa đạt 80 điểm)")
        return diem
    
sankhobao = san_kho_bau()
print(f"Điểm cuối cùng: {sankhobao}")



# Diem = [7.5, 8.0, 6.0, 9.0, 5.5, 8.5, 7.0, 6.5]

# def diemtrungbinh(Diem):
#     tong = 0
#     for value in Diem:
#         tong += value
#     tb = tong / len(Diem)
#     return tb

# tinhdiem = diemtrungbinh(Diem)
# print(f"Điểm trung bình là: {tinhdiem}")

# def Diemcaonhat(Diem):
#     max = Diem[0]
#     for value in Diem:
#         if value > max:
#             max = value
#     return max
# tinhdiem = Diemcaonhat(Diem)
# print(f"Điểm cao nhất là: {tinhdiem}")


# def Demsodiem(Diem):
#     lon = 0
#     nho = 0
#     for value in Diem:
#         if value >= 8:
#             lon += 1
#         else:
#             nho += 1
#     return lon,nho

# demsodiem = Demsodiem(Diem)
# print (f"Điểm từ 8 là: {demsodiem[0]}")
# print (f"Điểm nhỏ hơn 8 là: {demsodiem[1]}")
