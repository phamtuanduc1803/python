import math
u=int(input("Up:"))
d=int(input("Down:"))
l=int(input("Left:"))
r=int(input("Right:"))
x=u-d
y=r-l
kc=int(math.sqrt(x**2+y**2))
print("Khoang cach tu vi tri moi den vi tri ban dau la:",kc)
