import math

x = float(input("Nhap x: "))

if x >= 1:
    f = pow(2, x) + 3 * x + 4
elif x < 1:
    f = pow(3, x) + 2 * x + 1

print(f"f({x})= {round(f, 4)}")
