try:
    So = int(input("Nhập số: "))
except:
    print ("Lỗi nhập")
else:
# So = int(input("Nhập số: "))
    if So %2 ==0:
        print (f"{So} Là số chẵn")
    else:
        print (f"{So} Là số lẽ")
