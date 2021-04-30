def decipher(cipher):
    r=""
    i=0
    while i<len(cipher):
        s=""
        s+=cipher[i]
        s+=cipher[i+1]
        if int(s)>=97 and int(s)<=99:
            r+=chr(int(s))
            i=i+2
        else:
            s+=cipher[i+2]
            r+=chr(int(s))
            i=i+3
    return r
print(decipher("1229798"))
