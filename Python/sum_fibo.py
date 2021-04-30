def fiboSum(n):
    fibo=[1,2]
    sumFibo=3
    while sumFibo<=n:
        fibo.append(fibo[len(fibo)-2]+fibo[len(fibo)-1])
        sumFibo+=fibo[len(fibo)-1]
    index=len(fibo)-1
    while sumFibo!=n:
        if sumFibo-fibo[index]>=n:
            sumFibo-=fibo[index]
            fibo.pop(index)
        index-=1
    if len(fibo)==0:
        return [-1]
    else:
        return fibo
print(fiboSum(12907825))
