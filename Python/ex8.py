import math
def giaiptbac2(a,b,c):
    delta=b*b-4*a*c
    if delta<0:
        print ('phuong trinh vo nghiem')
    elif delta==0:
        x=(-b)/(2*a)
        print('Nghiem duy nhat :',x)
    else:
        x1=((-b)-math.sqrt(delta))/(2*a)
        x2=((-b)+math.sqrt(delta))/(2*a)
        print ('2 nghiem rieng biet : ',x1,x2)
a=int(input('Nhap a: '))
b=int(input('Nhap b: '))
c=int(input('Nhap c: '))
giaiptbac2(a,b,c)
