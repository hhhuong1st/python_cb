try:
    Nam = int(input('Nhập năm: '))
    Can = Nam % 10
    Chi = Nam % 12
except:
    print("Giá trị không hợp lệ")
else:
    match Can:
        case 0:
            print("Canh")
        case 1:
            print("Tân")
        case 2:
            print("Nhâm")
        case 3:
            print("Quý")
        case 4:
            print("Giáp")
        case 5:
            print("Ất")
        case 6:
            print("Bính")
        case 7:
            print("Đinh")
        case 8:
            print("Mậu")
        case 9:
            print("Kỷ")

    match Chi:
        case 0:
            print("Thân")
        case 1:
            print("Dậu")
        case 2:
            print("Tuất")
        case 3:
            print("Hợi")
        case 4:
            print("Tí")
        case 5:
            print("Sửu")
        case 6:
            print("Dần")
        case 7:
            print("Mão")
        case 8:
            print("Thìn")
        case 9:
            print("Tỵ")
        case 10:
            print("Ngọ")
        case 11:
            print("Mùi")