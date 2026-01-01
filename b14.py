import math

GPA = float(input("Nhap GPA(4): "))
if GPA >= 0 and GPA <= 4:
    result = GPA * 10 / 4
    print(f"GPA(10) = {result}")
else:
    print("Khong thoa man")