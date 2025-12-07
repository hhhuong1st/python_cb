# print("== Câu 4 ==")
# i=1
# dem = 0
# while(i<=10):
#     try:
#         so = int(input(f"Nhập số thứ {i}: "))
#         i += 1
#         if (so<0):
#             dem += 1
#     except ValueError:
#         print("Lỗi kiểu dữ liệu")
# print (f"Có {dem} số âm")

# 
# i=1
# min = 100000000
# max = -100000000

# while(i<=5):
#     try:
#         x = int(input(f"Nhập số thứ {i}: "))
#         i += 1
#         if x < min:
#             min = x
#         if x > max:
#             max = x
#     except ValueError:
#         print("Lỗi kiểu dữ liệu")
# print("Số nhỏ nhất:", min)
# print("Số lớn nhất:", max)

import math
print("== Câu 12 ==")
n = (input('Nhập để đếm ký tự chữ cái và số: '))
chucai = 0
chuso = 0
for ch in n:
    if ch.isalpha():
        chucai += 1
    elif ch.isdigit():
        chuso += 1
print("Số ký tự là chữ cái:", chucai)
print("Số ký tự là chữ số:", chuso)
    