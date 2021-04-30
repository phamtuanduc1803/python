res=[]
l=int(input())
for i in range(l):
    n=int(input())
    res.append(n)
def evenNum(res):
    r=[]
    for i in res:
        if i%2==0:
            r.append(i)
    print(r)
evenNum(res)
