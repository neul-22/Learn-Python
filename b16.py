from math import sqrt

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

if a > 0 or a < 0:
    tmp = b * b - 4 * a * c
    if tmp < 0:
        print("Phuong trinh vo nghiem")
    elif tmp == 0:
        x = -b / 2 * a
        print(f"Phuong trinh co nghiem kep x = {x}")
    elif tmp > 0:
        x1 = (-b + sqrt(tmp)) / 2 * a
        x2 = (-b - sqrt(tmp)) / 2 * a
        print(f"Phuong trinh co 2 nghiem phan biet x1 = {x1}, x2 = {x2}")
else:
    print("Khong hop le")