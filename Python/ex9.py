total=0
count=0
maxi= None
mini= None
while True:
    num=input('Enter a  number: ')
    if num=='done':
        break
    try:
        n=int(num)
        total=total+n
        count=count+1
        if maxi is None or maxi < n:
            maxi=n
        if mini is None or mini >n :
            mini=n
    except:
        print('Invalid input')
average=total/count
print(total,count,maxi,mini,average)
