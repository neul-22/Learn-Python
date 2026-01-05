from math import sqrt

n = int(input("Nhap n: "))
if n < 0:
    print("Khong hop le")
elif n == 1:
    print("1 khong phai la so nguyen to")
else:
    temp = True
    canbac2 = int(sqrt(n))
    for i in range(2, canbac2 + 1):
        if n % i == 0:
            temp = False
            break
    if temp == True:
        print(f"{n} la so nguyen to")
    else:
        print(f"{n} khong phai la so nguyen to")