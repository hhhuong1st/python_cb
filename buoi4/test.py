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

print("== Câu 9 ==")
so = int(input("Nhập số để đếm chữ số: "))

so1 = so
dem = 0
while(so != 0):
    so = so //10
    dem +=1 
print (f"Số {so1} có {dem} chữ số")