import math

n = int(input("Nhap n: "))
x = float(input("Nhap x: "))

if n <= 0:
    print('Khong hop le')
else:
    result = 0
    for i in range (0 , n + 1):
        result = result + x ** i
    print(f"F(x)= {result}")
