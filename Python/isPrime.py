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
            k++
        return factorSum(sum)
print (factorSum(24))
