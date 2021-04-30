def maxWater(arr):
    max_water=0
    for i in range(0,len(arr)-1):
        m=0
        m1=arr[i]
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                m1=max(m1,arr[i]*(j-i))
                m=max(m,m1)
            else:
                m1=max(m1,arr[j]*(j-i))
                m=max(m,m1)
        max_water=max(max_water,m)
    return max_water
arr=[1,8,6,2,5,4,8,3,7]
print(maxWater(arr))

    
