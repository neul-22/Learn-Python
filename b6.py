from math import sqrt

z = complex(input("Nhap z: "))
a = z.real
b = z.imag
result = sqrt(a * a + b * b)
print(f"Gia tri cua z = {result}")