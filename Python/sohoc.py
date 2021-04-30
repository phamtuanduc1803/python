def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def factorSum(n):
    if isPrime(n) is True:
        return n
    else:
        k=2
        sum=0
        while(n>1):
            while(n%k==0):
                sum+=k
                n/=k
            k+=1
        return factorSum(sum)
def maxFraction(tu,mau):
    indexmax=0
    for i in range(0,len(tu)):
        if (tu[indexmax]*mau[i]-mau[indexmax]*tu[i])<0:
            indexmax=i
    return indexmax
def lastDigitDiffZero(n):
    i=2
    a=1
    while i<=n:
        a*=i
        i+=1
        while a%10==0:
            a/=10
    while a%10==0:
        a=a/10
    return a%10
def digitsProduct(product):
    if product==0:
        return 10
    i=0
    p=0
    n=9
    while n>1:
        if product==1:
            break
        if product%n==0:
            p+=n*10**i
            i+=1
            product/=n
            n+=1
        n-=1
    if p==0:
        return -1
    return p
def pagesNumbering(n):
    j=1
    p=n
    while p/10 > 1:
        p/=10
        j+=1
    a=(n-10**(j-1)+1)*j
    j-=1
    while j>0:
        a+=(10**j-10**(j-1))*j
        j-=1
    return a
print(pagesNumbering(11))
    

