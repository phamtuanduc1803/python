a=raw_input('Nhap day so nhi phan : ')
ds=a.split(',')
b=[]
for x in ds:
    y=int(x,2)
    if y % 5 == 0:
        b.append(x)
print ",".join(b)
    
        
