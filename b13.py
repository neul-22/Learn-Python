import math

year = int(input("Nhap nam can kiem tra: "))

if year < 1582:
    print(f"{year} khong tinh theo lich Gregorius")
elif year / 400 == 0 or (year / 100 != 0 and year / 4 == 0):
    print(f"{year} la nam nhuan")

else:
    print(f"{year} la nam khong nhuan")