import math
A = int(input('Nhập A: '))
B = int(input('Nhập B: '))
C = int(input('Nhập C: '))


if (A + B > C and A + C > B and B + C > A and A > 0 and B > 0 and C > 0): 
    Cv = A + B + C
    P =Cv/2
    Dt = math.sqrt(P*(P-A)*(P-B)*(P-C))
    print (f" Chu vi = {Cv} - Diện tích = {Dt}")
else:
    print ('Không phải là tam giác')      