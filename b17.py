h = int(input("Nhap so gio: "))
m = int(input("Nhap so phut: "))

if (h < 0 or h > 23):
    print("Khong hop le")
elif (m < 0 or m > 59):
    print("Khong hop le")
else:
    if (h == 12):
        print(f"{h}:{m} PM")
    elif (h > 12):
        h = h % 12
        print(f"{h}:{m} AM")
    else:
        print(f"{h}:{m} AM")