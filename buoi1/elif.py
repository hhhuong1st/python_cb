import math
A = int(input("Nhập A: "))
B = int(input("Nhập B: "))
C = int(input("Nhập C: "))

delta = B**2 - (4*A*C)

if delta < 0:
    print ('Phương trình vô nghiệm')
elif delta ==0:
    x = -B / (2*A)
    print ( f'Phương trình có 2 nghiệm kép X1 = X2: {x}')
else:
    x1 = (-B + math.sqrt(delta)) / 2*A
    x2 = (-B - math.sqrt(delta)) / 2*A
    print ( f'Phương trình có 2 nghiệm phân biệt X1 = {x1} X2: {x2}')