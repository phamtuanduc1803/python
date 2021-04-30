import math
class giaiptb2:
    "Nhap cac he so de giai phuong trinh bac 2"
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.d=b**2-4*a*c
    def giai(self):
        if self.d>0:
            self.x1=(self.b*(-1)-math.sqrt(self.d))/(2*self.a)
            self.x2=(self.b*(-1)+math.sqrt(self.d))/(2*self.a)
            print 'Phuong trinh co 2 nghiem la : ',self.x1,' ',self.x2
        elif self.d==0:
            self.x=(b*(-1))/(2*a)
            print 'Phuong trinh co nghiem duy nhat la : ',self.x
        else:
            print 'Phuong trinh vo nghiem'
            
a=int(input('Nhap a : '))
b=int(input('Nhap b : '))
c=int(input('Nhap c : '))
p=giaiptb2(a,b,c)
p.giai()
