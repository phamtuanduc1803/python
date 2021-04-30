res=[]
l=int(input())
for i in range(l):
    n=int(input())
    res.append(n)
s=""
while True:
    if res[0]==0:
        res.pop(0)
    else:
        break
for i in  res:
    s+=str(i)
print(s)
