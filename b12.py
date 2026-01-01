import math

canh = float(input("Nhap canh: "))
if canh > 0:
    dt = pow(canh, 2)
    print(f"Dien tich cua hinh vuong = {round(dt, 3)}")
else:
    print("Error")