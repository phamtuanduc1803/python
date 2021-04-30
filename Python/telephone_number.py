def telephoneNumber(s):
    if len(s)>=11 and len(s)<=100:
        for i in range(0,len(s)):
            if len(s)-i <11:
                return False
            elif s[i]=='8':
                return True
    else:
        return False
print(telephoneNumber("88888888888"))
