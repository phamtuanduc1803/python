def minimumAbsolute(arr):
    arr.sort()
    r=[]
    tmp=arr[1]-arr[0]
    for i in range(0,len(arr)-1):
        if arr[i+1]-arr[i]==tmp:
            a=[]
            a.append(arr[i])
            a.append(arr[i+1])
            r.append(a)
    return r
print(minimumAbsolute([1,2,11,3,6,9,10,12,15]))
