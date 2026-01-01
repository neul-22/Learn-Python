import math

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))

if a > 0 or a < 0:
    x = -b / a
    print("Phuong trinh co 1 nghiem")
    print(f"Gia tri cua x = {x}")
elif a == 0 and b == 0:
    print("Phuong trinh co vo so nghiem")
else:
    print("Phuong trinh vo nghiem")