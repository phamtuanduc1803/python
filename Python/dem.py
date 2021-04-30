def commonCharacterCount(s1,s2):
    f1=[0]*25
    f2=[0]*25
    for i in s1:
        f1[ord(i)-97]+=1
    for i in s2:
        f2[ord(i)-97]+=1
    r=0
    print(f2)
    for i in range(0,len(f1)):
        if f1[i]==f2[i]:
            r+=f1[i]
        if f1[i]>f2[i]:
            r+=f2[i]
        if f1[i]<f2[i]:
            r+=f1[i]
    return r

def differentValuesInMultiplicationTable2(n,m):
    p=n*m
    check=[0]*p
    r=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if check[i*j-1]==0:
                check[i*j-1]+=1
                r+=1
    return r

def checkEqualFrequency(inputArray):
    return True if len(set(inputArray.count(i) for i in inputArray))==1 else False

def differentSymbolsNaive(s):
    return len(set(s))

def differentSubstringsTrie(inputString):
    arr=[]
    for i in range(1,len(inputString)+1):
        for j in range(len(inputString)):
            if inputString[j:j+i] not in arr:
                arr.append(inputString[j:j+i])
    return len(arr)

def charactersRearrangement(string1,string2):
    if len(string1)!=len(string2):
        return False
    arr1=[0]*25
    arr2=[0]*25
    for i in string1:
        arr1[ord(i)-97]+=1
    for i in string2:
        arr2[ord(i)-97]+=1
    if arr1==arr2:
        return True
    return False

def charactersRearrangement2(string1,string2):
    return sorted(string1)==sorted(string2) #sorted(doi tuong,key,reverse) sap xep

def isPangram(sentence):
    a=97
    while a<=112:
        if chr(a) in sentence:
            a+=1
        else :
            return False
    return True

def differentSquares(matrix):
    a=[]
    for i in range(len(matrix)-1):
        for j in range(len(matrix[1])-1):
            b=[]
            b.append(matrix[i][j])
            b.append(matrix[i][j+1])
            b.append(matrix[i+1][j])
            b.append(matrix[i+1][j+1])
            if b not in a:
                a.append(b)
    return len(a)

    
    

