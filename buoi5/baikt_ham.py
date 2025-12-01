def NhapN():
    while True:
        try:
            n = int(input("Nhập số N: "))
            if n > 0:
                return n
            else:
                print("N phải > 0")
        except ValueError:
            print("Lỗi kiểu dữ liệu")

def xuat(N):
    for i in range (1, N+1):
        print ("*"*i)

def sohh(N):
    tong = 0
    for i in range (1,N):
        if N % i == 0:
            tong += i
    if tong == N:
        return True
    return False
