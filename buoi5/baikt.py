import baikt_ham

print("Nhập N: ")
n = baikt_ham.NhapN()

baikt_ham.xuat(n)

print("Nhập số để kiểm tra số hoàn hảo: ")
So = baikt_ham.NhapN()

if baikt_ham.sohh(So):
    print(f"Số {So} là số hoàn hảo")
else:
    print(f"Số {So} không là số hoàn hảo")
