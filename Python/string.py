def checkStrongPassword(password):
    if (len(password)>=6):
        kt1=False
        kt2=False
        kt3=False
        kt4=False
        for i in password:
            if '0'<=i<='9':
                kt1=True
            if 'a'<=i<='z':
                kt2=True
            if 'A'<=i<='Z':
                kt3=True
            if '!'<=i<='+':
                kt4=True
        return kt1 and kt2 and kt3 and kt4
    return False
def amendTheSentence(s):
    r=""
    for i in s:
        if i.isupper():
            r+=" "+i.lower()
        else:
            r+=i
    r=r.strip() # strip() dung de loai bo cac ki tu thua o dau va cuoi,mac dinh la space
    return r
def checkPalindrome(inputString):
    j=len(inputString)-1
    for i in inputString:
        if i==inputString[j]:
            j-=1
        else:
            return False
    return True
def formatString(inputt):
    return ' '.join(inputt.split())

def truncateString(s):
    i=0
    j=len(s)-1
    while i<j:
        if int(s[i])%3==0:
            i+=1
            continue
        if int(s[j])%3==0:
            j-=1
            continue
        if (int(s[i])+int(s[j]))%3==0:
            i+=1
            j-=1
            continue
        break
    return s[i:j+1]

def stringsCrossover(inputArray,result):
    r=0
    for i in range(0,len(inputArray)):
        for j in range(i+1,len(inputArray)):
            k=0
            while k<len(result):
                if inputArray[i][k]==result[k] or inputArray[j][k]==result[k]:
                    k+=1
                else:
                    break
            if k==len(result):
                r+=1
    return r

def questionCorrection(s):
    s1=' '.join(s.split())
    s1=s1.lower()
    print(s1)
    r=""
    r+=s1[0:1].upper()
    for i in range(1,len(s1)-1):
        if 'a'<=s1[i]<='z' or 'A'<=s1[i]<='Z' or '0'<=s1[i]<='9' or s1[i]==',' or s1[i]==' ' or s1[i]=='?':
            if s1[i]==' ' and s1[i+1]==',':
                continue
            if s1[i]==' ' and s1[i+1]=='?':
                continue
            if s1[i]=='?' and i<len(s1)-1:
                continue
            if s1[i]==',' and s1[i+1]=='?':
                continue
            if s1[i-1]==',' and s1[i]!=' ':
                r+=" "
            r+=s1[i]
        else:
                r+=""
    r+="?"
    return r

def lineEncoding(s):
    arr=[]
    c=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            c+=1
        else:
            arr.append(str(c)+s[i-1])
            c=1
    arr.append(str(c)+s[len(s)-1])
    return ''.join(arr)

