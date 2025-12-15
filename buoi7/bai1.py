import bai1_ham
Diem = [7.5,8.0,6.0,9.0,5.5,8.5,7.0,6.5]

# Câu 1
print(f"Điểm trung bình là: {bai1_ham.diemtrungbinh(Diem)}")
# Câu 2
print (f"Điểm cao nhất là: {bai1_ham.Diemcaonhat(Diem)}")
# Câu 3
demsodiem = bai1_ham.Demsodiem(Diem)
print (f"Điểm từ 8 là: {demsodiem[0]}")
print (f"Điểm nhỏ hơn 8 là: {demsodiem[1]}")

# Câu 4
print(f"Sắp xếp danh sách tăng dần: {bai1_ham.Sapxeptangdan(Diem)}")


















# Diem = [7.5,8.0,6.0,9.0,5.5,8.5,7.0,6.5]
# # a
# tong = 0
# for value in Diem:
#     tong += value
#     tb = tong / len(Diem)
# print (f"Điểm trung bình là: {tb}")
# # b
# max = Diem[0]
# for value in Diem:
#     if value > max:
#         max = value
# print (f"Điểm cao nhất là: {max}")
# # c
# lon = 0
# nho = 0
# for value in Diem:
#     if value >= 8:
#         lon += 1
#     else:
#         nho += 1
# print (f"Đếm số điểm >= 8.0 là: {lon}")
# print (f"Đếm số điểm < 8.0 là: {nho}")
# # d
# for i in range (len(Diem)):
#     for j in range (i + 1, len(Diem)):
#         if Diem[i] > Diem[j]:
#             Diem[i], Diem[j] = Diem[j], Diem[i]
# print (Diem) 
