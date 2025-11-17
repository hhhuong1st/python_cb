Thang = int(input('Nhập tháng: '))

match Thang:
    case 2|3|4:
        print ('Mùa Xuân')
    case 5|6|7:
        print ('Mùa Hạ')
    case 8|9|10:
        print ('Mùa Thu')
    case 11|12|1:
        print ('Mùa Đông')
    case _:
        print ('Không đúng giá trị')
    