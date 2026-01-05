n = int(input("Nhap n: "))
if n < 0:
    print("Khong hop le")
elif n == 0:
    print("0! = 1")
else:
    count = 1
    for i in range(1, n + 1):
        count *= i
    print(f"{n}! = {count}")
