
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
