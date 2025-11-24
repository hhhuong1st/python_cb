while True:
    try:
        n = int (input("Nhập n: "))
        if(n>0):
            break
    except ValueError:
        print ("Lỗi kiểu dữ liệu")

print("== Câu 1 ==")
for i in range (1, n+1):
    if i%2==0:
        print(i,end=" ")



print("== Câu 2 ==")
tong = 0
for i in range(1,n+1):
    if (i%2 !=0):
        tong +=i
print(f" Tổng các số lẻ từ 1 đến N là: {tong}")



print("== Câu 3 ==")
for i in range(1,n):
        if i%3 ==0:
            print(i, end =" ")



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



print("== Câu 5 ==")
for i in range(1,n):
    print(f"{n} x {i} = {n * i}")



print("== Câu 6 ==")
for i in range(1, n + 1):
    if i == 5:
        continue
    print(i)



print("== Câu 8 ==")
i=1
min = 100000000
max = -100000000

while(i<=n):
    try:
        x = int(input(f"Nhập số thứ {i}: "))
        i += 1
        if x < min:
            min = x
        if x > max:
            max = x
    except ValueError:
        print("Lỗi kiểu dữ liệu")
print(f"Số nhỏ nhất: {min}")
print(f"Số nhỏ nhất: {max}")