count={}
s=input("Nhap chuoi:")
for i in s.split(" "):
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i in count:
    print("%s %s"%(i,count[i]))
