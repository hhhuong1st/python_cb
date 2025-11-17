try:
    Thang = int(input('Nhập tháng: '))
except:
    print ("Giá trị không hợp lệ")
else:
    match Thang:
        case 1|3|5|7|8|10|12:
            print ('Có 31 ngày')
        case 2:
            print ('Có 28 ngày hoặc 29 ngày')
        case 4|6|9|11:
            print ('Có 30 ngày')
        case _:    
            print (f"Không có tháng: {Thang}")
        
