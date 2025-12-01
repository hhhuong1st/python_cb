def sont(so):
    if so <=1:
        return False
    for i in range (2, so):
        if so%i ==0:
            return False
    return True

