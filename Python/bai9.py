import math
item=raw_input("Nhap cac so d : ").split(' ')
c=50
h=30
print item
for d in item:
    d=float(d)
    q=(int)(math.sqrt(2*c*d/h))
    print q
