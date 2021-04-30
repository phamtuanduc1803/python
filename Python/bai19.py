x=raw_input('Nhap day so : ')
ds=x.split(',')
d=[]
for i in ds:
    a=int(i)
    if a % 2 !=0:
        d.append(i)
print ",".join(d)
