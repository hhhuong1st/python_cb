import random
# Câu 1:
def tinhtiennuoc(x):
    if x <= 0:
        return None
    tiennuoc = 0
    if x <= 10:
        tiennuoc = x * 7000
    elif x <= 20:
        tiennuoc = 10 * 7000 + (x - 10) * 9000
    else:
        tiennuoc = 10 * 7000 + 10 * 9000 + (x - 20) * 12000
    phimoitruong = tiennuoc * 0.05
    tongtien = tiennuoc + phimoitruong
    return tongtien

# Câu 2:
diem = 0
for i in range (1,7):
    print ("=> Lượt", i)
    if random.random()<0.6:
        diemcong=random.randint(5,30)
        diem += diemcong
        print(f"Tìm thấy kho báo, được cộng {diemcong} điểm") 
    else:
        diem = diem -2
        if(diem<=0):
            diem = 0
            print ("Không tìm thấy trừ 2 điểm")
    print(f"Tổng điểm {diem}")
    if (diem>=80):
        print ("Thắng")
if(diem<80):
    print ("Thua")

# Câu 3:
# a
def diemtrungbinh(Diem):
    tong = 0
    for value in Diem:
        tong += value
        tb = tong / len(Diem)
    return tb 

# b
def Diemcaonhat(Diem):
    max = Diem[0]
    for value in Diem:
        if value > max:
            max = value
    return max

# c
def Demsodiem(Diem):
    lon = 0
    nho = 0
    for value in Diem:
        if value >= 8:
            lon += 1
        else:
            nho += 1
    return lon,nho
# d
def Sapxeptangdan(Diem):
    for i in range (len(Diem)):
        for j in range (i + 1, len(Diem)):
            if Diem[i] > Diem[j]:
                Diem[i], Diem[j] = Diem[j], Diem[i]
    return Diem
