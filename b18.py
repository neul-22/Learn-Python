n = int(input("Nhap n: "))
if n < 1:
    print("Khong hop le")
else:
    count = 0
    for i in range (1, n + 1):
        if (i % 2 == 0):
            count += i
    print(count)
