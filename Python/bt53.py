a=int(input())
b=int(input())
def gcd(a,b):
    if a>b:
        if a%b==0:
            return b
        else:
            return gcd(b,a%b)
    elif a<b:
        if b%a==0:
            return a
        else:
            return gcd(a,b%a)
    else:
        return 1
print(gcd(a,b))
