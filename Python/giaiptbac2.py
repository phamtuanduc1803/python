import math
print 'Nhap cac he so a,b,c: '
a=float(input())
b=float(input())
c=float(input())
d=b*b-4*a*c
if d<0:
    print 'Phuong trinh vo nghiem'
elif d==0:
    x=b/(2*a)
    print 'Nghiem kep ',x
else:
    x1=((-1)*b-math.sqrt(d))/(2*a)
    x2=((-1)*b+math.sqrt(d))/(2*a)
    print 'Nghiem thu nhat :',x1
    print 'Nghiem thu hai :',x2
