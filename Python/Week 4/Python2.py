def garders(*garder):
    total = 0
    teedad = 0
    for num in garder:
        total += num 
        teedad += 1 
    miangin = total / teedad
    return miangin
print(garders(1, 5, 9, 7, 3))