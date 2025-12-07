while True:
    try:
        n = int (input("Nhập n: "))
        if(n>0):
            break
    except ValueError:
        print ("Lỗi kiểu dữ liệu")

###########################

print("== Câu 1 ==")
for i in range (1, n+1):
    if i%2==0:
        print(i,end=" ")

############################

print("== Câu 2 ==")
tong = 0
for i in range(1,n+1):
    if (i%2 !=0):
        tong +=i
print(f" Tổng các số lẻ từ 1 đến N là: {tong}")

############################

print("== Câu 3 ==")
for i in range(1,n):
        if i%3 ==0:
            print(i, end =" ")

############################

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

############################

print("== Câu 5 ==")
for i in range(1,n):
    print(f"{n} x {i} = {n * i}")

############################

print("== Câu 6 ==")
for i in range(1, n + 1):
    if i == 5:
        continue
    print(i)

############################

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
print(f"Số lớn nhất: {max}")

############################

print("== Câu 9 ==")
so = int(input("Nhập số để đếm chữ số: "))
so1 = so
dem = 0
while(so != 0):
    so = so //10
    dem +=1 
print (f"Số {so1} có {dem} chữ số")

############################

print("== Câu 10 ==")
n = int(input('Nhập số lượng phần tử Fibonacci: '))
a = 0
b = 1
for i in range (n):
    print (a)
    c = a + b
    a = b
    b = c 

print("== Câu 11 ==")
n = int(input('Nhập để kiểm tra số hoàn hảo: '))
tong = 0
for i in range (1, n):
    if n%i == 0:
        tong += i
if tong == n:
    print (f'{n} là số hoàn hảo')
else:
    print (f'{n} không là số hoàn hảo')


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