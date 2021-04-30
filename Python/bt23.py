def bt23(n):
    for i in range(n):
        if i%7==0:
            yield i
n=int(input("Nhap so n: "))
for i in bt23(n):
    print(i)
